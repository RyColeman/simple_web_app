import cPickle as pickle


def build_model(filename):
    ### write your code to build a model
    vectorizer, model = None, None
    return vectorizer, model


if __name__ == '__main__':
    vectorizer, model = build_model('data/articles.csv')
    with open('data/vectorizer.pkl', 'w') as f:
        pickle.dump(vectorizer, f)
    with open('data/model.pkl', 'w') as f:
        pickle.dump(model, f)
