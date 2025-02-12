from typing import Any, Optional
from flet.core.control import Control, OptionalNumber

class FletLocalisation(Control):
    """
    FletLocalisation Control, das nur String-Daten zurückgibt.
    """

    def __init__(
        self,
        value: Optional[str] = None,
        tooltip: Optional[str] = None,
        opacity: OptionalNumber = None,
        visible: Optional[bool] = None,
        data: Any = None,
    ):
        super().__init__(
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
        )
        self.value = value

    def _get_control_name(self):
        return "flet_localisation"

    @property
    def value(self) -> Optional[str]:
        return self._get_attr("value", "")

    @value.setter
    def value(self, value: Optional[str]):
        self._set_attr("value", str(value) if value is not None else "")
