from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", cache_dir="cache"
)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", cache_dir="cache"
)


generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
results = generator("Good Morning, ")
print(results)
