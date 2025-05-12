from server.config import *
from llm_calls import *
from utils.rag_utils import rag_call
import json

user_message = "Can you exmplan what is co-living?"

### EXAMPLE 1: Router ###
# Classify the user message to see if we should answer or not
router_output = classify_input(user_message)
if router_output == "Refuse to answer":
    llm_answer = "Sorry, I can only answer questions about architecture."

else:
    print(router_output)
    ### EXAMPLE 2: Simple call ###
    # simple call to LLM, try different sys prompt flavours
    brainstorm = generate_concept(user_message)
    print(brainstorm)

    ### EXAMPLE 4: Structured Output ###
    # extract the architecture attributes from the user
    # parse a structured output with regex
    attributes = extract_attributes(brainstorm)
    print(attributes)

    attributes = attributes.strip()
    attributes = json.loads(attributes)
    spatial_features, lifestyle_themes, target_users = (attributes[k] for k in ("spatial_features", "lifestyle_themes", "target_users"))

    ### EXAMPLE 3: Chaining ###
    brutalist_question = create_question(lifestyle_themes)
    print(brutalist_question)
    # call llm with the output of a previous call

    ### EXAMPLE 5: RAG ####
    # Get a response based on the knowledge found
    rag_result= rag_call(brutalist_question, embeddings = "knowledge/the_rise_of_co-living.json", n_results = 10)
    print(rag_result)