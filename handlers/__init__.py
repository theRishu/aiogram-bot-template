from .start import start_router
from .help import help_router
from .admin import admin_router
from .echo import echo_router


routers_list =[
    start_router,
    admin_router,
    other_router,
    echo_router #This must be last
]