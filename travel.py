class Travel:
    
    def __init__(self):
        self.ref_number = None
        self.disclosure_group = None
        self.title_en = None
        self.title_fr = None
        self.name = None
        self.purpose_en = None
        self.purpose_fr = None
        self.start_date = None
        self.end_date = None
        self.destination_en = None
        self.destination_fr = None
        self.airfare = None
        self.other_transport = None
        self.lodging = None
        self.meals = None
        self.other_expenses = None
        self.total = None
        self.additional_comments_en = None
        self.additional_comments_fr = None
        self.owner_org = None
        self.owner_org_title = None

    @classmethod
    def get_data(cls):
        return cls.__dict__
    
    def print(self):
        all_objects = self.get_data()
        for data in all_objects:
            print(f"[{data}: {all_objects[data]}]")

        # print(
        #     f"[ref_number: {self.ref_number}, disclosure_group: {self.disclosure_group}, title_en: {self.title_en}, title_fr: {self.title_fr}, "
        #     f"name: {self.name}, purpose_en: {self.purpose_en}, purpose_fr: {self.purpose_fr}, "
        #     f"start_date: {self.start_date}, end_date: {self.end_date}, destination_en: {self.destination_en}, "
        #     f"destination_fr: {self.destination_fr}, airfare: {self.airfare}, other_transport: {self.other_transport}, lodging: {self.lodging}, "
        #     f"meals: {self.meals}, other_expenses: {self.other_expenses}, total: {self.total},"
        #     f"additional_comments_en: {self.additional_comments_en}, additional_comments_fr: {self.additional_comments_fr}, owner_org: {self.owner_org},"
        #     f"owner_org_title: {self.owner_org_title}]")

