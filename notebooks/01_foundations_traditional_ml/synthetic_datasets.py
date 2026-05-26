"""
Synthetic actuarial datasets with a known Bayes-optimal target.

Both generators return a tidy ``pandas.DataFrame`` that includes the ground-truth
conditional mean (``true_mean`` for regression) or probability
(``true_p_lapse`` for classification). Drop that column before fitting any model,
and use it afterwards as the irreducible benchmark against which every fitted
model can be compared. The data-generating processes are deterministic given the
random seed.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def make_regression_dataset(n: int = 20_000, seed: int = 42) -> pd.DataFrame:
    """Synthetic MTPL portfolio with annual claim cost as the target.

    The target is generated from a log-normal severity model whose conditional
    mean ``E[claim_cost | X]`` is exposed as the ``true_mean`` column. Pop that
    column before fitting and use it later as the Bayes-optimal benchmark.

    Parameters
    ----------
    n : int
        Number of policies to draw.
    seed : int
        Seed for the random number generator (deterministic output).

    Returns
    -------
    pandas.DataFrame
        Columns: ``driver_age``, ``vehicle_age``, ``vehicle_power``,
        ``annual_mileage``, ``bonus_malus``, ``region``, ``claim_cost``,
        ``true_mean``.
    """
    rng = np.random.default_rng(seed)

    driver_age = (18 + rng.beta(2.0, 2.5, size=n) * 62).round().astype(int)
    vehicle_age = np.clip(rng.exponential(scale=6.0, size=n), 0, 25).round().astype(int)
    vehicle_power = np.clip(rng.normal(loc=110, scale=35, size=n), 40, 250).round().astype(int)
    annual_mileage = np.exp(rng.normal(loc=np.log(12_000), scale=0.45, size=n))
    bonus_malus = np.clip(rng.normal(loc=100, scale=25, size=n), 50, 200).round().astype(int)
    region_levels = np.array(["North", "South", "East", "West", "Center"])
    region = rng.choice(region_levels, size=n, p=[0.22, 0.20, 0.18, 0.20, 0.20])

    region_effect = {"North": -0.05, "South": 0.10, "East": -0.02, "West": 0.05, "Center": 0.00}
    region_offset = np.vectorize(region_effect.get)(region)

    log_mu = (
        5.50
        - 0.15 * (driver_age - 40) / 20
        + 0.20 * vehicle_age / 10
        + 0.35 * vehicle_power / 100
        + 0.30 * np.log(annual_mileage / 12_000)
        + 0.25 * (bonus_malus - 100) / 50
        + region_offset
        + 0.10 * (driver_age < 25).astype(float)
    )

    sigma = 0.7
    noise = rng.normal(loc=0.0, scale=sigma, size=n)
    claim_cost = np.exp(log_mu + noise)
    true_mean = np.exp(log_mu + 0.5 * sigma ** 2)

    return pd.DataFrame(
        {
            "driver_age": driver_age,
            "vehicle_age": vehicle_age,
            "vehicle_power": vehicle_power,
            "annual_mileage": annual_mileage.round(0),
            "bonus_malus": bonus_malus,
            "region": region,
            "claim_cost": claim_cost.round(2),
            "true_mean": true_mean,
        }
    )


def make_classification_dataset(n: int = 20_000, seed: int = 42) -> pd.DataFrame:
    """Synthetic lapse-prediction portfolio with an ~21 % positive rate.

    The Bernoulli probability of lapse is exposed as ``true_p_lapse``. Pop that
    column (and ``lapse``) before fitting and use it later as the Bayes-optimal
    benchmark for log-loss.

    Parameters
    ----------
    n : int
        Number of policies to draw.
    seed : int
        Seed for the random number generator (deterministic output).

    Returns
    -------
    pandas.DataFrame
        Columns: ``tenure_years``, ``policyholder_age``, ``annual_premium``,
        ``premium_increase_pct``, ``payment_frequency``, ``n_claims_last_3y``,
        ``channel``, ``lapse``, ``true_p_lapse``.
    """
    rng = np.random.default_rng(seed)

    tenure_years = np.clip(rng.exponential(scale=5.0, size=n), 0, 25)
    policyholder_age = np.clip(rng.normal(loc=46, scale=14, size=n), 18, 85).round().astype(int)
    annual_premium = np.exp(rng.normal(loc=np.log(800), scale=0.35, size=n)).round(2)
    premium_increase_pct = np.clip(rng.normal(loc=0.04, scale=0.06, size=n), -0.05, 0.30)
    payment_levels = np.array(["monthly", "quarterly", "annual"])
    payment_frequency = rng.choice(payment_levels, size=n, p=[0.55, 0.20, 0.25])
    n_claims_last_3y = rng.poisson(lam=0.4, size=n).clip(max=5)
    channel_levels = np.array(["broker", "direct", "online", "tied_agent"])
    channel = rng.choice(channel_levels, size=n, p=[0.30, 0.25, 0.20, 0.25])

    payment_effect = {"monthly": 0.35, "quarterly": 0.05, "annual": -0.30}
    channel_effect = {"broker": -0.10, "direct": 0.10, "online": 0.30, "tied_agent": -0.20}
    payment_offset = np.vectorize(payment_effect.get)(payment_frequency)
    channel_offset = np.vectorize(channel_effect.get)(channel)

    # Intercept tuned so the empirical positive rate lands near 21 %.
    logit_p = (
        -1.40
        + 0.25 * (policyholder_age - 45) / 20
        - 0.60 * tenure_years / 10
        + 5.0 * premium_increase_pct
        + 0.20 * (n_claims_last_3y - 1) / 2
        + payment_offset
        + channel_offset
        + 0.40 * premium_increase_pct * (tenure_years < 2).astype(float)
    )

    true_p_lapse = 1.0 / (1.0 + np.exp(-logit_p))
    lapse = (rng.uniform(size=n) < true_p_lapse).astype(int)

    return pd.DataFrame(
        {
            "tenure_years": tenure_years.round(2),
            "policyholder_age": policyholder_age,
            "annual_premium": annual_premium,
            "premium_increase_pct": premium_increase_pct.round(4),
            "payment_frequency": payment_frequency,
            "n_claims_last_3y": n_claims_last_3y,
            "channel": channel,
            "lapse": lapse,
            "true_p_lapse": true_p_lapse,
        }
    )
