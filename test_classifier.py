from ml.classifier import TextClassifier

classifier = TextClassifier()

sample = """
Page 1

Machine Learning

Figure 5

Machine learning is changing healthcare.

www.school.edu

Conclusion
"""

filtered = classifier.filter_text(sample)

print(filtered)