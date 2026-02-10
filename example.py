import pickle

model = pickle.load(open('model/model.pkl', 'rb'))

characteristics = [1.423e+01, 1.710e+00, 2.430e+00, 1.560e+01, 1.270e+02, 2.800e+00,
  3.060e+00, 2.800e-01, 2.290e+00, 5.640e+00, 1.040e+00, 3.920e+00,
  1.065e+03]
# characteristics = [14.13, 4.1, 2.74, 24.5, 96, 2.05, 0.76, 0.56, 1.35, 9.2, 0.61, 1.6, 560]
y_pred = model.predict([characteristics])

print(f"The category of wine for the provided characteristics is {y_pred}")
