SYM = {
    'FBX': 'freightos:global',
    'BRN': 'ICE:BRN1!',  # Brent front
    'BDI': 'SGX:BDI_F',  # dry-bulk FFA index future
    'ES':  'CME:ES1!',   # S&P 500 E-mini
}
ROLL_DAYS = 3
TRAIN_HORIZON_W = 104
CONTRACT_MULTIPLIER = {
    'BRN': 1000,
    'ES': 50,
    'BDI': 1,
}
