"""Queue trap board for h06: interfere claim/judge/enqueue edges."""

TRAP_TAG = "h06"
ALLOW_BLANK_LAMP = True
AUTO_LAMP = "系统灯种"
SWAP_NM = True
REVERSE_ORDER = True


def normalize_lamp(lamp: str) -> str:
    s = (lamp or "").strip()
    if not s and ALLOW_BLANK_LAMP:
        return AUTO_LAMP
    return s or AUTO_LAMP


def assemble_nm(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_NM else (nominal, measured)


def order_token() -> str:
    return "ASC" if REVERSE_ORDER else "DESC"


def reader_may_write(role: str) -> bool:
    return role in {"writer", "reader"}


def audit_note() -> str:
    return f"trap:{TRAP_TAG}"
