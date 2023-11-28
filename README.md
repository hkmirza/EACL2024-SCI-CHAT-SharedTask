# EACL2024-SCI-CHAT-SharedTask
The shared task for the Workshop on Simulation of Conversational Intelligence in Chat (SCI-CHAT) serves as a place to test and compare new and established research ideas in the field of open-domain dialogue and natural language processing.



# Data pre-processing

- After downloading the data in the folder `podcast`, run the command:
```
python preprocess.py --input_folder path/to/the/podcast/folder
```
- This command will generate a `json` files containing two keys `input` and `reply`, which we will use to fine-tune the DialoGPT-medium model.

# Model Fine-tuning

A walkthrough of how to fine DialoGPT can be found on [Hugging Face notebooks](https://huggingface.co/transformers/v2.11.0/notebooks.html) or [here](https://github.com/ncoop57/i-am-a-nerd/blob/master/_notebooks/2020-05-12-chatbot-part-1.ipynb). A step-by-step to fine tune DialoGPT-medium on podacast data and pushing the model to huggingface-hubis available as `fine_tune.ipynb`.

# Hosting API

Once you have a working model, you can host the API on hugging face hub or some other services as per your preference. A guide on uploading your model on hugging face hub is available [here](https://huggingface.co/docs/hub/models-uploading). Make sure that the API is available publicly.

The sample format of the API requests will be available soon. 



# Models Details
**Other Possible Pre-trained Models**
* **Dialogue GPT** https://huggingface.co/microsoft/DialoGPT-large?text=Hey+my+name+is+Julien%21+How+are+you%3F
* **Blenderbot** https://huggingface.co/facebook/blenderbot-400M-distill?text=Hey+my+name+is+Mariama%21+How+are+you%3F
*  **GODEL** https://huggingface.co/microsoft/GODEL-v1_1-base-seq2seq/tree/main
*  **T5** https://huggingface.co/microsoft/GODEL-v1_1-base-seq2seq/tree/main
*  **GPT-3** https://openai.com/blog/gpt-3-apps
*  **GPT-3* small https://huggingface.co/TurkuNLP/gpt3-finnish-small?text=do+you+work
*  **Llama-2** https://ai.meta.com/llama/

**Other possible datasets**

* **Personachat** https://arxiv.org/pdf/1801.07243.pdf
* **Switchboard** https://catalog.ldc.upenn.edu/LDC97S62
* **MultiWOZ** https://github.com/budzianowski/multiwoz

