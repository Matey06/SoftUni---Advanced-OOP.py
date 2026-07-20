from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        self.adding_to_list(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        self.adding_to_list(topic, self.topics)

    def add_document(self, document: Document) -> None:
        self.adding_to_list(document, self.documents)

    def edit_category(self, category_id: int, new_name: str) -> None:
        curr_cat_id = next((i for i in self.categories if i.id == category_id), None)
        if curr_cat_id:
            curr_cat_id.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        curr_topic_id = next((i for i in self.topics if i.id == topic_id), None)
        if curr_topic_id:
            curr_topic_id.topic = new_topic
            curr_topic_id.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        curr_doc_id = next((i for i in self.documents if i.id == document_id), None)
        if curr_doc_id:
            curr_doc_id.file_name = new_file_name

    def  delete_category(self, category_id) -> None:
        curr_cat_id = next((i for i in self.categories if i.id == category_id), None)
        if curr_cat_id:
            self.categories.remove(curr_cat_id)

    def delete_topic(self, topic_id) -> None:
        curr_top_id = next((i for i in self.topics if i.id == topic_id), None)
        if curr_top_id:
            self.topics.remove(curr_top_id)

    def delete_document(self, document_id) -> None:
        curr_doc_id = next((i for i in self.documents if i.id == document_id), None)
        if curr_doc_id:
            self.documents.remove(curr_doc_id)

    def get_document(self, document_id: int) -> str | None:
        curr_doc_id = next((i for i in self.documents if i.id == document_id), None)
        if curr_doc_id:
            return repr(curr_doc_id)
        return None

    def __repr__(self) -> str:
        result = []
        for doc in self.documents:
            result.append(repr(doc))
        return '\n'.join(result)

    @staticmethod
    def adding_to_list(obj, list_to_add) -> None:
        if obj not in list_to_add:
            list_to_add.append(obj)