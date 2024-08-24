from langchain_core.pydantic_v1 import BaseModel, Field

# define the model
class SuggestionResponse(BaseModel):
    suggestion: str = Field(description="positive suggestion for negative habits")
    reason: str = Field(description="reason for suggesting it")
    plan_of_action: str = Field(description="plan to achieve the suggestion")