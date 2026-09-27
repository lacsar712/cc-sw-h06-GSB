TOLERANCE_NM = 0.08
# 压线浮点余量：录入精度为 0.01 nm，1e-9 只吸收二进制浮点尾差，
# 保证偏差恰好 0.08 nm 的压线样条判定为合格，而不会放到 0.0801。
_BORDER_EPS = 1e-9


def judge(nominal: float, measured: float) -> tuple[str, str]:
    delta = abs(measured - nominal)
    if delta <= TOLERANCE_NM + _BORDER_EPS:
        return "合格", f"偏差 {delta:.4f} nm 在允差内"
    return "超差", f"偏差 {delta:.4f} nm 超过允差 {TOLERANCE_NM}"
