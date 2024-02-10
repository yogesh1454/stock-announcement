class EventProcessor:

    _event = [
        'bonus',
        'rights',
        'split',
        'split.',
        'merger'
        'buyback'
        'bonus issue',
        'rights issue',
        'stock split',
        'bonus/share split/dividend',
        'offer for sale',
        'merger',
        'dividend declaration',
        'stock merger or acquisition',
        'spin-off',
        'share buyback',
        'corporate restructuring',
        'reverse stock split'
        ]

    def apply(self, announcement):
        result = False
        print ("calling event processor for: ", announcement['desc'])

        for event in self._event:
            if announcement['desc'] is not None and event in announcement['desc'].lower():
                result=True
            if announcement['attchmntFile'] is not None and event in announcement['attchmntFile'].lower():
                result=True
            if announcement['sm_name'] is not None and event in announcement['sm_name'].lower():
                result=True
            if announcement['attchmntText'] is not None and event in announcement['attchmntText'].lower():
                result=True

        return result

    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return len(lst3)>0

    def __init__(self):
        print("Event Processor initiallized ...")
