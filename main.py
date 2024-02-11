from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    summary = ""
    original_text = ""
    if request.method == 'POST':
        original_text = request.form['text']
        # Here you would integrate your text summarization logic
        summary = summarize_text(original_text)  # Placeholder for the actual summarization function
    return render_template('index.html', summary=summary, original_text=original_text)


def summarize_text(text):
    # Placeholder function for text summarization
    # Replace this with your actual summarization code
    return text[:100] + '...'


if __name__ == '__main__':
    app.run(debug=True)
