import numpy as np


from ml.model import train_model, inference, save_model, load_model


def test_train_model():
    """Test that the model trains successfully."""
    X_train = np.array([
        [25, 1],
        [35, 0],
        [45, 1],
        [55, 0],
    ])
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert model is not None
    assert hasattr(model, "predict")


def test_inference():
    """Test that inference returns predictions."""
    X_train = np.array([
        [25, 1],
        [35, 0],
        [45, 1],
        [55, 0],
    ])
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)
    predictions = inference(model, X_train)

    assert len(predictions) == len(X_train)
    assert set(predictions).issubset({0, 1})


def test_save_and_load_model(tmp_path):
    """Test that a trained model can be saved and loaded."""
    X_train = np.array([
        [25, 1],
        [35, 0],
        [45, 1],
        [55, 0],
    ])
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)
    model_path = tmp_path / "test_model.pkl"

    save_model(model, model_path)
    loaded_model = load_model(model_path)

    assert loaded_model is not None
    assert np.array_equal(
        inference(model, X_train),
        inference(loaded_model, X_train),
    )
