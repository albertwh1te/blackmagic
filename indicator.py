# -*- coding: utf-8 -*-
# this program is used for stock indicator based on talib and PyAlgoTrade where independent of PAT
# we just refer to the idea that PAT indicator developed with talib

"""
Created on Wed Mar 29 09:14:13 2017

@author: ZhouHuaxi
"""

from __future__ import division
import talib
import numpy


# Returns the last values of a dataseries as a numpy.array, or None if not enough values could be retrieved from the dataseries.
def value_ds_to_numpy(ds, count):
    ret = None
    try:
        values = ds[count * -1:]
        ret = numpy.array([float(value) for value in values])
    except IndexError:
        pass
    except TypeError:  # In case we try to convert None to float.
        pass
    return ret


# Returns the last open values of a bar dataseries as a numpy.array, or None if not enough values could be retrieved from the dataseries.
def bar_ds_open_to_numpy(barDs, count):
    return value_ds_to_numpy(barDs.getOpenDataSeries(), count)


# Returns the last high values of a bar dataseries as a numpy.array, or None if not enough values could be retrieved from the dataseries.
def bar_ds_high_to_numpy(barDs, count):
    return value_ds_to_numpy(barDs.getHighDataSeries(), count)


# Returns the last low values of a bar dataseries as a numpy.array, or None if not enough values could be retrieved from the dataseries.
def bar_ds_low_to_numpy(barDs, count):
    return value_ds_to_numpy(barDs.getLowDataSeries(), count)


# Returns the last close values of a bar dataseries as a numpy.array, or None if not enough values could be retrieved from the dataseries.
def bar_ds_close_to_numpy(barDs, count):
    return value_ds_to_numpy(barDs.getCloseDataSeries(), count)


# Returns the last volume values of a bar dataseries as a numpy.array, or None if not enough values could be retrieved from the dataseries.
def bar_ds_volume_to_numpy(barDs, count):
    return value_ds_to_numpy(barDs.getVolumeDataSeries(), count)


# Calls a talib function with the last values of a dataseries.
def call_talib_with_ds(ds, count, talibFunc, *args, **kwargs):
    data = value_ds_to_numpy(ds, count)
    if data is None:
        return None
    return talibFunc(data, *args, **kwargs)  # 前面是可多个的数值参数，后面是名字参数


# hlcv: High, Low, Close and Volume.
def call_talib_with_hlcv(barDs, count, talibFunc, *args, **kwargs):
    high = bar_ds_high_to_numpy(barDs, count)
    if high is None:
        return None

    low = bar_ds_low_to_numpy(barDs, count)
    if low is None:
        return None

    close = bar_ds_close_to_numpy(barDs, count)
    if close is None:
        return None

    volume = bar_ds_volume_to_numpy(barDs, count)
    if volume is None:
        return None

    return talibFunc(high, low, close, volume, *args, **kwargs)


def call_talib_with_hlc(barDs, count, talibFunc, *args, **kwargs):
    high = bar_ds_high_to_numpy(barDs, count)
    if high is None:
        return None

    low = bar_ds_low_to_numpy(barDs, count)
    if low is None:
        return None

    close = bar_ds_close_to_numpy(barDs, count)
    if close is None:
        return None

    return talibFunc(high, low, close, *args, **kwargs)


def call_talib_with_ohlc(barDs, count, talibFunc, *args, **kwargs):
    open_ = bar_ds_open_to_numpy(barDs, count)
    if open_ is None:
        return None

    high = bar_ds_high_to_numpy(barDs, count)
    if high is None:
        return None

    low = bar_ds_low_to_numpy(barDs, count)
    if low is None:
        return None

    close = bar_ds_close_to_numpy(barDs, count)
    if close is None:
        return None

    return talibFunc(open_, high, low, close, *args, **kwargs)


def call_talib_with_hl(barDs, count, talibFunc, *args, **kwargs):
    high = bar_ds_high_to_numpy(barDs, count)
    if high is None:
        return None

    low = bar_ds_low_to_numpy(barDs, count)
    if low is None:
        return None

    return talibFunc(high, low, *args, **kwargs)


######################################################################
## talib wrappers

def AD(barDs, count):
    """Chaikin A/D Line"""
    return call_talib_with_hlcv(barDs, count, talib.AD)


def ADOSC(barDs, count, fastperiod=-2 ** 31, slowperiod=-2 ** 31):
    """Chaikin A/D Oscillator"""
    return call_talib_with_hlcv(barDs, count, talib.ADOSC, fastperiod, slowperiod)


def ADX(barDs, count, timeperiod=-2 ** 31):
    """Average Directional Movement Index"""
    return call_talib_with_hlc(barDs, count, talib.ADX, timeperiod)


def ADXR(barDs, count, timeperiod=-2 ** 31):
    """Average Directional Movement Index Rating"""
    return call_talib_with_hlc(barDs, count, talib.ADXR, timeperiod)


def APO(ds, count, fastperiod=-2 ** 31, slowperiod=-2 ** 31, matype=0):
    """Absolute Price Oscillator"""
    return call_talib_with_ds(ds, count, talib.APO, fastperiod, slowperiod, matype)


def AROON(barDs, count, timeperiod=-2 ** 31):
    """Aroon"""
    ret = call_talib_with_hl(barDs, count, talib.AROON, timeperiod)
    if ret is None:
        ret = (None, None)
    return ret


def AROONOSC(barDs, count, timeperiod=-2 ** 31):
    """Aroon Oscillator"""
    return call_talib_with_hl(barDs, count, talib.AROONOSC, timeperiod)


def ATR(barDs, count, timeperiod=-2 ** 31):
    """Average True Range"""
    return call_talib_with_hlc(barDs, count, talib.ATR, timeperiod)


def AVGPRICE(barDs, count):
    """Average Price"""
    return call_talib_with_ohlc(barDs, count, talib.AVGPRICE)


def BBANDS(ds, count, timeperiod=-2 ** 31, nbdevup=-4e37, nbdevdn=-4e37, matype=0):
    """Bollinger Bands"""
    ret = call_talib_with_ds(ds, count, talib.BBANDS, timeperiod, nbdevup, nbdevdn, matype)
    if ret is None:
        ret = (None, None, None)
    return ret


def BETA(ds1, ds2, count, timeperiod=-2 ** 31):
    """Beta"""
    data1 = value_ds_to_numpy(ds1, count)
    if data1 is None:
        return None
    data2 = value_ds_to_numpy(ds2, count)
    if data2 is None:
        return None
    return talib.BETA(data1, data2, timeperiod)


def BOP(barDs, count):
    """Balance Of Power"""
    return call_talib_with_ohlc(barDs, count, talib.BOP)


def CCI(barDs, count, timeperiod=-2 ** 31):
    """Commodity Channel Index"""
    return call_talib_with_hlc(barDs, count, talib.CCI, timeperiod)


def CDLMOVEAVERAGE(barDS, count):
    """Moving Average queue Up/Down"""
    timeperiod = numpy.array([5, 10, 20, 30])

    close = bar_ds_close_to_numpy(barDS, count)
    if close is None:
        return None

    candle = numpy.zeros(count)

    if close is not None and count >= timeperiod[3]:
        MA5 = SMA(close, count, timeperiod[0])
        MA10 = SMA(close, count, timeperiod[1])
        MA20 = SMA(close, count, timeperiod[2])
        MA30 = SMA(close, count, timeperiod[3])

        for i in range(timeperiod[3] - 1, len(close)):
            if MA5[i] > MA10[i] > MA20[i] > MA30[i]:
                candle[i] = 100
            elif MA5[i] < MA10[i] < MA20[i] < MA30[i]:
                candle[i] = -100

    return candle.astype(int)


def CMO(ds, count, timeperiod=-2 ** 31):
    """Chande Momentum Oscillator"""
    return call_talib_with_ds(ds, count, talib.CMO, timeperiod)


def CORREL(ds1, ds2, count, timeperiod=-2 ** 31):
    """Pearson's Correlation Coefficient (r)"""
    data1 = value_ds_to_numpy(ds1, count)
    if data1 is None:
        return None
    data2 = value_ds_to_numpy(ds2, count)
    if data2 is None:
        return None
    return talib.CORREL(data1, data2, timeperiod)


def DEMA(ds, count, timeperiod=-2 ** 31):
    """Double Exponential Moving Average"""
    return call_talib_with_ds(ds, count, talib.DEMA, timeperiod)


def DX(barDs, count, timeperiod=-2 ** 31):
    """Directional Movement Index"""
    return call_talib_with_hlc(barDs, count, talib.DX, timeperiod)


def EMA(ds, count, timeperiod=10):
    """Exponential Moving Average"""

    assert timeperiod > 1  # 窗口参数必须大于1，否则抛异常

    mid = numpy.ones(count + timeperiod - 1)
    mid[:timeperiod - 1] = mid[:timeperiod - 1] * ds[0]
    mid[timeperiod - 1:] = ds
    EMA = call_talib_with_ds(mid, count + timeperiod - 1, talib.EMA, timeperiod)
    EMA[timeperiod - 1] = ds[0]
    return EMA[timeperiod - 1:]


def HT_DCPERIOD(ds, count):
    """Hilbert Transform - Dominant Cycle Period"""
    return call_talib_with_ds(ds, count, talib.HT_DCPERIOD)


def HT_DCPHASE(ds, count):
    """Hilbert Transform - Dominant Cycle Phase"""
    return call_talib_with_ds(ds, count, talib.HT_DCPHASE)


def HT_PHASOR(ds, count):
    """Hilbert Transform - Phasor Components"""
    ret = call_talib_with_ds(ds, count, talib.HT_PHASOR)
    if ret is None:
        ret = (None, None)
    return ret


def HT_SINE(ds, count):
    """Hilbert Transform - SineWave"""
    ret = call_talib_with_ds(ds, count, talib.HT_SINE)
    if ret is None:
        ret = (None, None)
    return ret


def HT_TRENDLINE(ds, count):
    """Hilbert Transform - Instantaneous Trendline"""
    return call_talib_with_ds(ds, count, talib.HT_TRENDLINE)


def HT_TRENDMODE(ds, count):
    """Hilbert Transform - Trend vs Cycle Mode"""
    return call_talib_with_ds(ds, count, talib.HT_TRENDMODE)


def KAMA(ds, count, timeperiod=-2 ** 31):
    """Kaufman Adaptive Moving Average"""
    return call_talib_with_ds(ds, count, talib.KAMA, timeperiod)


def LINEARREG(ds, count, timeperiod=-2 ** 31):
    """Linear Regression"""
    return call_talib_with_ds(ds, count, talib.LINEARREG, timeperiod)


def LINEARREG_ANGLE(ds, count, timeperiod=-2 ** 31):
    """Linear Regression Angle"""
    return call_talib_with_ds(ds, count, talib.LINEARREG_ANGLE, timeperiod)


def LINEARREG_INTERCEPT(ds, count, timeperiod=-2 ** 31):
    """Linear Regression Intercept"""
    return call_talib_with_ds(ds, count, talib.LINEARREG_INTERCEPT, timeperiod)


def LINEARREG_SLOPE(ds, count, timeperiod=-2 ** 31):
    """Linear Regression Slope"""
    return call_talib_with_ds(ds, count, talib.LINEARREG_SLOPE, timeperiod)


def MA(ds, count, timeperiod=-2 ** 31, matype=0):
    """All Moving Average"""
    return call_talib_with_ds(ds, count, talib.MA, timeperiod, matype)


def MACD(ds, count, fastperiod=-2 ** 31, slowperiod=-2 ** 31, signalperiod=-2 ** 31):
    """Moving Average Convergence/Divergence"""
    ret = call_talib_with_ds(ds, count, talib.MACD, fastperiod, slowperiod, signalperiod)
    if ret is None:
        ret = (None, None, None)
    return ret


def MACDEXT(ds, count, fastperiod=-2 ** 31, fastmatype=0, slowperiod=-2 ** 31, slowmatype=0, signalperiod=-2 ** 31,
            signalmatype=0):
    """MACD with controllable MA type"""
    ret = call_talib_with_ds(ds, count, talib.MACDEXT, fastperiod, fastmatype, slowperiod, slowmatype, signalperiod,
                             signalmatype)
    if ret is None:
        ret = (None, None, None)
    return ret


def MACDFIX(ds, count, signalperiod=-2 ** 31):
    """Moving Average Convergence/Divergence Fix 12/26"""
    ret = call_talib_with_ds(ds, count, talib.MACDFIX, signalperiod)
    if ret is None:
        ret = (None, None, None)
    return ret


def MAMA(ds, count, fastlimit=-4e37, slowlimit=-4e37):
    """MESA Adaptive Moving Average"""
    ret = call_talib_with_ds(ds, count, talib.MAMA, fastlimit, slowlimit)
    if ret is None:
        ret = (None, None)
    return ret


def MAX(ds, count, timeperiod=-2 ** 31):
    """Highest value over a specified period"""

    assert timeperiod > 1
    max_value = call_talib_with_ds(ds, count, talib.MAX, timeperiod)
    for i in range(1, timeperiod - 1):
        max_value[i] = numpy.max(ds[0:i + 1])
    max_value[0] = ds[0]
    return max_value


def MAXINDEX(ds, count, timeperiod=-2 ** 31):
    """Index of highest value over a specified period"""
    return call_talib_with_ds(ds, count, talib.MAXINDEX, timeperiod)


def MEDPRICE(barDs, count):
    """Median Price"""
    return call_talib_with_hl(barDs, count, talib.MEDPRICE)


def MFI(barDs, count, timeperiod=-2 ** 31):
    """Money Flow Index"""
    return call_talib_with_hlcv(barDs, count, talib.MFI, timeperiod)


def MIDPOINT(ds, count, timeperiod=-2 ** 31):
    """MidPoint over period"""
    return call_talib_with_ds(ds, count, talib.MIDPOINT, timeperiod)


def MIDPRICE(barDs, count, timeperiod=-2 ** 31):
    """Midpoint Price over period"""
    return call_talib_with_hl(barDs, count, talib.MIDPRICE, timeperiod)


def MIN(ds, count, timeperiod=-2 ** 31):
    """Lowest value over a specified period"""

    assert timeperiod > 1
    min_value = call_talib_with_ds(ds, count, talib.MIN, timeperiod)
    for i in range(1, timeperiod - 1):
        min_value[i] = numpy.min(ds[0:i + 1])
    min_value[0] = ds[0]
    return min_value


def MININDEX(ds, count, timeperiod=-2 ** 31):
    """Index of lowest value over a specified period"""
    return call_talib_with_ds(ds, count, talib.MININDEX, timeperiod)


def MINMAX(ds, count, timeperiod=-2 ** 31):
    """Lowest and highest values over a specified period"""
    ret = call_talib_with_ds(ds, count, talib.MINMAX, timeperiod)
    if ret is None:
        ret = (None, None)
    return ret


def MINMAXINDEX(ds, count, timeperiod=-2 ** 31):
    """Indexes of lowest and highest values over a specified period"""
    ret = call_talib_with_ds(ds, count, talib.MINMAXINDEX, timeperiod)
    if ret is None:
        ret = (None, None)
    return ret


def MINUS_DI(barDs, count, timeperiod=-2 ** 31):
    """Minus Directional Indicator"""
    return call_talib_with_hlc(barDs, count, talib.MINUS_DI, timeperiod)


def MINUS_DM(barDs, count, timeperiod=-2 ** 31):
    """Minus Directional Movement"""
    return call_talib_with_hl(barDs, count, talib.MINUS_DM, timeperiod)


def MOM(ds, count, timeperiod=-2 ** 31):
    """Momentum"""
    return call_talib_with_ds(ds, count, talib.MOM, timeperiod)


def NATR(barDs, count, timeperiod=-2 ** 31):
    """Normalized Average True Range"""
    return call_talib_with_hlc(barDs, count, talib.NATR, timeperiod)


def OBV(ds1, volumeDs, count):
    """On Balance Volume"""
    data1 = value_ds_to_numpy(ds1, count)
    if data1 is None:
        return None
    data2 = value_ds_to_numpy(volumeDs, count)
    if data2 is None:
        return None
    return talib.OBV(data1, data2)


def PLUS_DI(barDs, count, timeperiod=-2 ** 31):
    """Plus Directional Indicator"""
    return call_talib_with_hlc(barDs, count, talib.PLUS_DI, timeperiod)


def PLUS_DM(barDs, count, timeperiod=-2 ** 31):
    """Plus Directional Movement"""
    return call_talib_with_hl(barDs, count, talib.PLUS_DM, timeperiod)


def PPO(ds, count, fastperiod=-2 ** 31, slowperiod=-2 ** 31, matype=0):
    """Percentage Price Oscillator"""
    return call_talib_with_ds(ds, count, talib.PPO, fastperiod, slowperiod, matype)


def ROC(ds, count, timeperiod=-2 ** 31):
    """Rate of change : ((price/prevPrice)-1)*100"""
    return call_talib_with_ds(ds, count, talib.ROC, timeperiod)


def ROCP(ds, count, timeperiod=-2 ** 31):
    """Rate of change Percentage: (price-prevPrice)/prevPrice"""
    return call_talib_with_ds(ds, count, talib.ROCP, timeperiod)


def ROCR(ds, count, timeperiod=-2 ** 31):
    """Rate of change ratio: (price/prevPrice)"""
    return call_talib_with_ds(ds, count, talib.ROCR, timeperiod)


def ROCR100(ds, count, timeperiod=-2 ** 31):
    """Rate of change ratio 100 scale: (price/prevPrice)*100"""
    return call_talib_with_ds(ds, count, talib.ROCR100, timeperiod)


def RSI(ds, count, timeperiod=-2 ** 31):
    """Relative Strength Index"""
    assert timeperiod > 0
    lc = ref(ds, 1)
    UP = ds - lc
    DN = numpy.abs(UP)
    UP[0] = 0
    UP[UP < 0] = 0
    rsi = SMA(UP, count, timeperiod) / SMA(DN, count, timeperiod) * 100
    rsi[rsi == numpy.inf] = 0
    return rsi


def SAR(barDs, count, acceleration=-4e37, maximum=-4e37):
    """Parabolic SAR"""
    return call_talib_with_hl(barDs, count, talib.SAR, acceleration, maximum)


def SAREXT(barDs, count, startvalue=-4e37, offsetonreverse=-4e37, accelerationinitlong=-4e37, accelerationlong=-4e37,
           accelerationmaxlong=-4e37, accelerationinitshort=-4e37, accelerationshort=-4e37, accelerationmaxshort=-4e37):
    """Parabolic SAR - Extended"""
    return call_talib_with_hl(barDs, count, talib.SAREXT, startvalue, offsetonreverse, accelerationinitlong,
                              accelerationlong, accelerationmaxlong, accelerationinitshort, accelerationshort,
                              accelerationmaxshort)


def SMA(ds, count, timeperiod=-2 ** 31, weight=1):
    """Simple Moving Average"""
    assert timeperiod > 0 and timeperiod > weight  # N必须大于0,且N>M
    assert count > timeperiod  # 传入的数据数量大于N窗口数量
    df = value_ds_to_numpy(ds, count)
    SMA = numpy.ones(count) * numpy.nan
    start = len(df[numpy.isnan(df)])
    if start < count:
        SMA[start] = df[start]
        for i in range(start + 1, count):
            SMA[i] = (weight * df[i] + (timeperiod - weight) * SMA[i - 1]) / timeperiod
        SMA[start] = 0
    return SMA


def STDDEV(ds, count, timeperiod=-2 ** 31, nbdev=-4e37):
    """Standard Deviation"""
    return call_talib_with_ds(ds, count, talib.STDDEV, timeperiod, nbdev)


def STD(ds, count, timeperiod=-2 ** 31, nbdev=-4e37):
    """Standard Deviation /n-1"""
    assert timeperiod > 1  # 否则分母为0，抛异常
    STDDEV = call_talib_with_ds(ds, count, talib.STDDEV, timeperiod, nbdev)
    STD = STDDEV * (timeperiod / (timeperiod - 1)) ** 0.5
    return STD


def STOCH(barDs, count, fastk_period=-2 ** 31, slowk_period=-2 ** 31, slowk_matype=0, slowd_period=-2 ** 31,
          slowd_matype=0):
    """Stochastic"""
    ret = call_talib_with_hlc(barDs, count, talib.STOCH, fastk_period, slowk_period, slowk_matype, slowd_period,
                              slowd_matype)
    if ret is None:
        ret = (None, None)
    return ret


def STOCHF(barDs, count, fastk_period=-2 ** 31, fastd_period=-2 ** 31, fastd_matype=0):
    """Stochastic Fast"""
    ret = call_talib_with_hlc(barDs, count, talib.STOCHF, fastk_period, fastd_period, fastd_matype)
    if ret is None:
        ret = (None, None)
    return ret


def STOCHRSI(ds, count, timeperiod=-2 ** 31, fastk_period=-2 ** 31, fastd_period=-2 ** 31, fastd_matype=0):
    """Stochastic Relative Strength Index"""
    ret = call_talib_with_ds(ds, count, talib.STOCHRSI, timeperiod, fastk_period, fastd_period, fastd_matype)
    if ret is None:
        ret = (None, None)
    return ret


def SUM(ds, count, timeperiod=-2 ** 31):
    """Summation"""
    return call_talib_with_ds(ds, count, talib.SUM, timeperiod)


def T3(ds, count, timeperiod=-2 ** 31, vfactor=-4e37):
    """Triple Exponential Moving Average (T3)"""
    return call_talib_with_ds(ds, count, talib.T3, timeperiod, vfactor)


def TEMA(ds, count, timeperiod=-2 ** 31):
    """Triple Exponential Moving Average"""
    return call_talib_with_ds(ds, count, talib.TEMA, timeperiod)


def TRANGE(barDs, count):
    """True Range"""
    return call_talib_with_hlc(barDs, count, talib.TRANGE)


def TRIMA(ds, count, timeperiod=-2 ** 31):
    """Triangular Moving Average"""
    return call_talib_with_ds(ds, count, talib.TRIMA, timeperiod)


def TRIX(ds, count, timeperiod=-2 ** 31):
    """1-day Rate-Of-Change (ROC) of a Triple Smooth EMA"""
    return call_talib_with_ds(ds, count, talib.TRIX, timeperiod)


def TSF(ds, count, timeperiod=-2 ** 31):
    """Time Series Forecast"""
    return call_talib_with_ds(ds, count, talib.TSF, timeperiod)


def TYPPRICE(barDs, count):
    """Typical Price"""
    return call_talib_with_hlc(barDs, count, talib.TYPPRICE)


def ULTOSC(barDs, count, timeperiod1=-2 ** 31, timeperiod2=-2 ** 31, timeperiod3=-2 ** 31):
    """Ultimate Oscillator"""
    return call_talib_with_hlc(barDs, count, talib.ULTOSC, timeperiod1, timeperiod2, timeperiod3)


def VAR(ds, count, timeperiod=-2 ** 31, nbdev=-4e37):
    """Variance"""
    return call_talib_with_ds(ds, count, talib.VAR, timeperiod, nbdev)


def WCLPRICE(barDs, count):
    """Weighted Close Price"""
    return call_talib_with_hlc(barDs, count, talib.WCLPRICE)


def WILLR(barDs, count, timeperiod=-2 ** 31):
    """Williams' %R"""
    return call_talib_with_hlc(barDs, count, talib.WILLR, timeperiod)


def WMA(ds, count, timeperiod=-2 ** 31):
    """Weighted Moving Average"""
    return call_talib_with_ds(ds, count, talib.WMA, timeperiod)


##计算金叉死叉，上下关系的调用函数
def cross(arr_a, arr_b):
    assert arr_a is not None
    assert arr_b is not None
    assert len(arr_a) == len(arr_b)
    length = len(arr_a)
    gold_cross = [False for _ in range(length)]
    death_cross = [False for _ in range(length)]
    for i in range(1, length):
        if arr_a[i] > arr_b[i] and arr_a[i - 1] < arr_b[i - 1]:
            gold_cross[i] = True
        elif arr_a[i] < arr_b[i] and arr_a[i - 1] > arr_b[i - 1]:
            death_cross[i] = True
    return gold_cross, death_cross


def cross_const(arr_a, n=0.0):
    assert arr_a is not None
    assert len(arr_a) > 0
    length = len(arr_a)
    gold_cross = [False for _ in range(length)]
    death_cross = [False for _ in range(length)]
    for i in range(1, length):
        if arr_a[i] > n and arr_a[i - 1] < n:
            gold_cross[i] = True
        elif arr_a[i] < n and arr_a[i - 1] > n:
            death_cross[i] = True
    return gold_cross, death_cross


def compare(arr_a, arr_b):
    assert arr_a is not None
    assert arr_b is not None
    assert len(arr_a) == len(arr_b)
    # length = len(arr_a)
    # cmp_g = [False for _ in range(length)]
    # cmp_l = [False for _ in range(length)]
    # for i in range(0, length):
    #     if arr_a[i] > arr_b[i]:
    #         cmp_g[i] = True
    #     elif arr_b[i] > arr_a[i]:
    #         cmp_l[i] = True
    return  arr_a > arr_b,arr_a<arr_b


##取上N天的数值
def ref(arr, n=1):
    assert arr is not None and len(arr) > n
    new_arr = numpy.ones(len(arr)) * numpy.nan
    new_arr[n:] = arr[:-n]
    return new_arr
