from states.meta.base_state import BaseState
from states.meta.state_enums import StateEnum


class LoaderState(BaseState, state_name=StateEnum.LOADER):
    def on_load(self, reload: bool) -> None:
        if reload:
            return

        # Add asset loading etc...
        self.manager.change_state(self.manager.post_init_state)
