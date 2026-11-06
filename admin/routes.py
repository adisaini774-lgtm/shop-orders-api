from fastapi import APIRouter

router = APIRouter()


@router.delete("/admin/orders/{order_id}")
def purge_order(order_id: str):
    return {"purged": order_id}

