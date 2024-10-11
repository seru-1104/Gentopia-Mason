from typing import Any
from gentopia.tools.basetool import *

class PregnancyNutritionArgs(BaseModel):
    stage: str = Field(..., description="The stage of pregnancy (first, second, or third trimester)")

class PregnancyNutrition(BaseTool):
    """Tool that provides pregnancy nutrition tips based on the trimester."""

    name = "pregnancy_nutrition"
    description = ("Provides nutrition tips for pregnant women depending on their trimester."
                   " Input should specify the trimester (first, second, or third).")

    args_schema: Optional[Type[BaseModel]] = PregnancyNutritionArgs

    def _run(self, stage: str) -> str:
        if stage.lower() == "first trimester":
            return (
                "First Trimester Nutrition Tips:\n"
                "- Focus on foods rich in folic acid (e.g., leafy greens, citrus fruits) to support early fetal development.\n"
                "- Ensure proper hydration by drinking at least 8 glasses of water per day.\n"
                "- Include lean protein (e.g., chicken, tofu, lentils) and whole grains in your diet.\n"
                "- Small, frequent meals can help with morning sickness.\n"
                "- Avoid foods high in mercury (e.g., certain types of fish) and unpasteurized dairy products."
            )
        elif stage.lower() == "second trimester":
            return (
                "Second Trimester Nutrition Tips:\n"
                "- Continue eating foods rich in iron (e.g., lean meats, beans, fortified cereals) to support increased blood volume.\n"
                "- Include calcium-rich foods (e.g., dairy products, leafy greens) for bone development.\n"
                "- Stay hydrated and consume fiber-rich foods to prevent constipation.\n"
                "- Focus on a balanced diet with plenty of fruits and vegetables.\n"
                "- Be mindful of healthy weight gain during this stage."
            )
        elif stage.lower() == "third trimester":
            return (
                "Third Trimester Nutrition Tips:\n"
                "- Increase intake of omega-3 fatty acids (e.g., fatty fish, flaxseeds) to support brain development.\n"
                "- Stay hydrated and eat fiber-rich foods to help with digestion.\n"
                "- Consume foods rich in protein (e.g., eggs, nuts, legumes) for muscle development.\n"
                "- Focus on small, frequent meals to prevent heartburn and indigestion.\n"
                "- Make sure to get enough calcium and vitamin D for strong bones and teeth."
            )
        else:
            return "Please specify a valid trimester (first, second, or third)."

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = PregnancyNutrition()._run("second trimester")
    print(ans)



