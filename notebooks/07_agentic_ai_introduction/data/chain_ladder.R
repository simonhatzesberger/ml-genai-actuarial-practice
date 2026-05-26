# Chain-ladder reserving on a 5x5 paid-loss triangle.
#
# Inputs:
#   triangle.csv -- wide-format loss triangle, one row per accident year,
#                   columns dev_1..dev_5 (cumulative paid losses in thousands EUR;
#                   NA for not-yet-observed development years).
#
# Outputs (printed to stdout in 'name: value' format for downstream tooling):
#   - five age-to-age development factors
#   - the cumulative-to-ultimate factor for each accident year
#   - the projected ultimate per accident year
#   - the IBNR reserve per accident year
#   - the total ultimate and total reserve

triangle_df <- read.csv("triangle.csv", stringsAsFactors = FALSE)

# Drop the accident_year column to get the loss matrix; keep AY as a vector.
ay <- triangle_df$accident_year
loss_matrix <- as.matrix(triangle_df[, paste0("dev_", 1:5)])

n_ay  <- nrow(loss_matrix)
n_dev <- ncol(loss_matrix)

# --- Step 1: age-to-age development factors --------------------------------
# f_{k} = sum(C_{i, k+1}) / sum(C_{i, k}) over rows i where both are observed.
dev_factors <- numeric(n_dev - 1)
for (k in 1:(n_dev - 1)) {
  num <- sum(loss_matrix[, k + 1], na.rm = TRUE)
  den <- sum(loss_matrix[!is.na(loss_matrix[, k + 1]), k])
  dev_factors[k] <- num / den
}
for (k in seq_along(dev_factors)) {
  cat(sprintf("dev_factor_%d: %.6f\n", k, dev_factors[k]))
}

# --- Step 2: cumulative-to-ultimate factor for each accident year ----------
# For AY i with observed columns up to k_i, CDF_i = product of dev_factors from k_i to n_dev-1.
cdf <- numeric(n_ay)
for (i in 1:n_ay) {
  observed_dev <- max(which(!is.na(loss_matrix[i, ])))
  if (observed_dev == n_dev) {
    cdf[i] <- 1.0
  } else {
    cdf[i] <- prod(dev_factors[observed_dev:(n_dev - 1)])
  }
}

# --- Step 3: ultimate and reserve per accident year ------------------------
ultimate <- numeric(n_ay)
paid_to_date <- numeric(n_ay)
reserve <- numeric(n_ay)
for (i in 1:n_ay) {
  observed_dev <- max(which(!is.na(loss_matrix[i, ])))
  paid_to_date[i] <- loss_matrix[i, observed_dev]
  ultimate[i] <- paid_to_date[i] * cdf[i]
  reserve[i] <- ultimate[i] - paid_to_date[i]
}
for (i in 1:n_ay) {
  cat(sprintf("ultimate_%d: %.4f\n", ay[i], ultimate[i]))
}
for (i in 1:n_ay) {
  cat(sprintf("reserve_%d: %.4f\n", ay[i], reserve[i]))
}

# --- Step 4: totals --------------------------------------------------------
ultimate_total <- sum(ultimate)
reserve_total <- sum(reserve)
cat(sprintf("ultimate_total: %.4f\n", ultimate_total))
cat(sprintf("reserve_total: %.4f\n", reserve_total))
