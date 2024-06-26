import pandas as pd
import numpy as np
import pandas_ta as ta
from ta.volatility import KeltnerChannel

class TechAnalysis:
    def __init__(self):
        self.ema_period = 13
        self.rsi_period = 7
        self.rsi_divergence_period = 14

    def calculate_technicals(self, df):
        try:
            df['EMA'] = ta.ema(df['CLOSE'], length=self.ema_period)
            df['RSI'] = ta.rsi(df['EMA'], length=self.rsi_period)
            df['RSI14'] = ta.rsi(df['CLOSE'], length=self.rsi_divergence_period)
            indicator_kc = KeltnerChannel(high=df["HIGH"], low=df["LOW"], close=df["CLOSE"], window=50, window_atr=50, fillna=False, multiplier=5, original_version=False)
            df["KC_UPPER"] = indicator_kc.keltner_channel_hband()
            df["KC_MIDDLE"] = indicator_kc.keltner_channel_mband()
            df["KC_LOWER"] = indicator_kc.keltner_channel_lband()
            df['AVG_VOLUME'] = df['VOLUME'].rolling(window=120, min_periods=1).mean()
            df['AVG_VOLUME_100'] = df['VOLUME'].rolling(window=100, min_periods=1).mean()
            df['AVG_VOLUME_70'] = df['VOLUME'].rolling(window=70, min_periods=1).mean()
            last_row = df.iloc[-1]
            return df
        except Exception as e:
            print('error while calculating technicals')
            print(f'exception occurred {e}')

TA = TechAnalysis()
