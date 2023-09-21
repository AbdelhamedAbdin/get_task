class Travel:
    
    def __init__(self, ref_number=None, disclosure_group=None, title_en=None, title_fr=None, name=None, purpose_en=None, purpose_fr=None,
                 start_date=None, end_date=None, destination_en=None, destination_fr=None, airfare=None, other_transport=None,
                 lodging=None, meals=None, other_expenses=None, total=None,
                 additional_comments_en=None, additional_comments_fr=None, owner_org=None, owner_org_title=None):
        self.ref_number = ref_number
        self.disclosure_group = disclosure_group
        self.title_en = title_en
        self.title_fr = title_fr
        self.name = name
        self.purpose_en = purpose_en
        self.purpose_fr = purpose_fr
        self.start_date = start_date
        self.end_date = end_date
        self.destination_en = destination_en
        self.destination_fr = destination_fr
        self.airfare = airfare
        self.other_transport = other_transport
        self.lodging = lodging
        self.meals = meals
        self.other_expenses = other_expenses
        self.total = total
        self.additional_comments_en = additional_comments_en
        self.additional_comments_fr = additional_comments_fr
        self.owner_org = owner_org
        self.owner_org_title = owner_org_title
    
    def print(self):
        all_objects = self.__dict__
        for data in all_objects:
            print(f"[{data}: {all_objects[data]}]", end=" ")

