from itemadapter import ItemAdapter


class DeleteHaoPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        fields = ['name', 'description']
        for field in fields:
            if adapter.get(field):
                adapter[field] = adapter[field].replace('\xa0', ' ')
        return item
