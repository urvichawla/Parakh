import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

class SkillLevelPredictor:
    def __init__(self):
        self.label_encoder = LabelEncoder()
        self.clf = DecisionTreeClassifier()

    def train(self, data):
        df = pd.DataFrame(data)
        
        df['level_encoded'] = self.label_encoder.fit_transform(df['level'])
        
        X = df[['level_encoded', 'correctness']]
        y = df['skill_level']

        self.clf.fit(X, y)

    def save_model(self, model_file):
        
        model_data = {
            'model': self.clf,
            'label_encoder': self.label_encoder
        }
        joblib.dump(model_data, model_file)

    def load_model(self, model_file):
        
        model_data = joblib.load(model_file)
        self.clf = model_data['model']
        self.label_encoder = model_data['label_encoder']

    def predict(self, level, correctness):
        
        level_encoded = self.label_encoder.transform([level])[0]

        new_question_data = pd.DataFrame({
            'level_encoded': [level_encoded],
            'correctness': [correctness]
        })

        
        predicted_skill_level = self.clf.predict(new_question_data)

        return predicted_skill_level[0]


if __name__ == "__main__":
    predictor = SkillLevelPredictor()


    data = {
        'level': ['beginner', 'intermediate', 'beginner', 'intermediate', 'advanced', 'advanced', 'intermediate', 'advanced','advanced','beginner','intermediate'],
        'correctness': [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        'skill_level': ['intermediate', 'beginner', 'intermediate', 'advanced', 'advanced', 'intermediate', 'advanced', 'intermediate','advanced','beginner','advanced']
    }

    predictor.train(data)


    model_file = "skill_level_model.pkl"
    predictor.save_model(model_file)
