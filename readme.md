# check4sexism

### Important

This is a tool that detects the "level" of sexism in a sentence, given as a percentage (so technically above 50% a text should be considered sexist and below that should not). To use the tool, once you've run the dockerfile locally, directing your browser to the url  to the url host:port/<text> should provide you with the percentage rating for <text>.  Please read endopoints.txt for more information.

Obviously this is not the best way to showcase things, but as I'm not the owner of the html\css\js template that was used to produce the final front-end result, this is the best I can do. I am only providing the the html\css\js code I created to alter the provided template, as an indication of my ability to code in the aforementioned languages.

However, for a complete front-end & back-end showcase of my work please visit https://research.swisscom.ai/demos/sexism-check/ 

### Definition of sexist language and a (tiny) technical summary

Sexist language is defined as that which demeans, ignores, or stereotypes members of either sex. In this demo, we are offering a natural language processing (NLP) tool which uses a neural network trained on a dataset consisting of sexist and non-sexist sentences. The sexist sentences have been collected after extracting specific parts of the posts found at https://everydaysexism.com/. The non-sexist sentences have been collected from subtitles of the British soap operas Eastenders and Doctors. Therefore, the detect level of sexism essentially measures "how close (far away) the given sentence is to the above sexist (non-sexist) sentences".

### In order to make the demo locally:

1. Build the back-end's docker file (from within the `~/sexism_check/back_end` folder).  

  ```sudo docker build -t sexism_check .```

2. Run the docker file. 

  ```sudo docker run -p 1313:1313 -ti sexism_check```.

3. The (local) url http://0.0.0.0:1313/your_text_to_check should display a number ranging from 0 to 100, which is the percentage of sexism detected by the tool in `your_text_to_check`.

### Folder contents

#### sexism_check

- `readme.md` - this file.
- `endpoints.txt` - explains the endpoints used and their function.
- *requirements.txt* - required packages and versions to run the Python code.

#### sexism_check/back_end

- *app.py* - Python script that runs the model.
- *Dockerfile* - instructions for Docker.
- *model.h5* - Keras's neural network setup and weights after training (h5 format).
- *requirements.txt* - required packages and versions.
- *texts* - collection of texts where the model was trained on, required by the tokenizer when evaluating new sentences (pickle format).

#### sexism_check/front_end

- `sexism_check.html`, modified and renamed version of `demo_name.html`.
- `sexism_check.js`, modified and renamed version of `demo_name.js`.
- `sexism_check.css`, modified and renamed version of `demo_name.css`.
- `research-icon.svg1`, the modified "grève des femmes" demo icon I used .

