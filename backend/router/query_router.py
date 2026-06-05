from fastapi import HTTPException,APIRouter
from services.process_query import process_query_service
from schema.question_schema import QueryRequest
from schema.query_response import QueryResponse

router=APIRouter()

@router.post("/query",response_model=QueryResponse)
async def query(request:QueryRequest):
    try:
       return process_query_service(request.question)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

