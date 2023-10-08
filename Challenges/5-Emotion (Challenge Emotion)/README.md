# Emotion (Challenge Emotion)

### Description of the challenge

---

The recognition of human emotions is a key element of human-computer interaction, and finds varied applications in fields such as virtual assistance technology, intelligent user interfaces and even mental health monitoring. This challenge aims to catalyze innovation by inviting participants to create AI models that not only recognize facial features, but can also interpret these visual cues to accurately assign emotional labels.

### What you will accomplish

---

The aim of this challenge is to identify the emotion on a person's face from an image. We have introduced a new task in this challenge that confronts participants with two kinds of images: clean and naturally degraded. To be more precise, we enhance the initial dataset of this challenge with naturally distorted images to simulate real-world scenarios. This has been achieved by mimicking conservative transformations such as rotation, scale, brightness and blur. Competitors in this task had to design a reliable and robust DL model that could accurately detect these types of images.

### Criteria for judgement

---

We score your submissions according to the F1 score and the robustness score. The score on the scoreboard is the harmonic mean between the f1 score and the robustness score. - Robustness is the f1 score of your prediction on perturbed data.

This challenge will require you to have a model that can accurately predict the emotion on a face, and also cope with robustness! To learn more about robustness, visit our website: https://codeml.ca or here's a description.

It is extremely difficult to test large-scale DL systems with millions of neurons and thousands of parameters for every conceivable input. DL system testing involves running a DL system to discover its vulnerabilities. The aim of these DL system experiments is to examine a variety of system properties. - Robustness is one of the most studied properties in DL systems. - Robustness refers to the DL system's ability to handle inputs of the worst-case scenario type. A human, for example, can recognize a car even if it's raining and the view is obstructed, whereas a DL system may make an erroneous prediction if similar image obstructions occur. To this end, the DL system must be trained to correctly identify an input in the presence of such external disturbances. These test scenarios are known as 'corner scenarios' and help to improve the robustness of DL systems.

A presentation of the method used by the winners will be requested. The code must also be provided.

- Accuracy
- F1_score
- Robustness
- Score
