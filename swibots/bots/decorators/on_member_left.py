from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnMemberLeft:
    def on_member_left(
        self: "swibots.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling members joins."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(swibots.bots.handlers.MemberLeftHandler(func, filter))

            return func

        return decorator
