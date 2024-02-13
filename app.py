from flask import Flask, request, render_template
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    summary = ""
    original_text = ""
    if request.method == 'POST':
        tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
        model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")

        original_text = "summarize: " + request.form['text']

        input_ids = tokenizer.encode(original_text, return_tensors="pt")
        summary_ids = model.generate(input_ids, max_length=200, min_length=75, length_penalty=2.0, num_beams=4, early_stopping=True)

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print(summary)

        # summarizer = pipeline("summarization", model="Falconsai/text_summarization")
        # summary = summarizer(original_text, max_length=150, min_length=50, do_sample=False)[0].get('summary_text')
        # print(summary)
    return render_template('index.html', summary=summary, original_text=original_text)


if __name__ == '__main__':
    app.run(debug=True)
