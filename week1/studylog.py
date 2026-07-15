import json
from pathlib import Path


class LogEntry:
    def __init__(self,date:str,topic:str,minutes:int,confidence:int,notes:str=""):
        self.date=date
        self.topic=topic
        if not minutes>=0:
            raise ValueError(f"Minutes should be always positive")
        self.minutes=minutes
        if not 1<= confidence <=5:
            raise ValueError(f"confidence must be 1 to 5 but we got {confidence}")
        self.confidence=confidence
        self.notes=notes
    def __repr__(self):
        return f"LogEntry({self.date},{self.topic},{self.minutes},{self.confidence},{self.notes})"
    def to_dict(self):
        return {"date":self.date,"topic":self.topic,"minutes":self.minutes
                ,"confidence":self.confidence,"notes":self.notes}
    @staticmethod
    def from_dict(data):
        return LogEntry(data["date"], data["topic"],data["minutes"],data["confidence"] ,data["notes"])

class StudyLog:
    def __init__(self,path):
        self.path=path
        self.entries=[]
        file_path=Path(self.path)
        try:
            if file_path.exists():
                data=json.loads(file_path.read_text())
                self.entries=[LogEntry.from_dict(item) for item in data]
        except FileNotFoundError:
            self.entries=[]
        except json.JSONDecodeError:
            print("Warning!corrupt file starting empty")
            self.entries=[]



        
    def add_entry(self,date:str,topic:str,minutes:int,confidence:int,notes:str=""):
        entry = LogEntry(date, topic, minutes, confidence, notes)
        self.entries.append(entry)
        data=[entry.to_dict() for entry in self.entries]
        Path(self.path).write_text(json.dumps(data,indent=4))

    def summary(self):
        total_minutes=sum(entry.minutes for entry in self.entries)
        total_hours=total_minutes / 60
        total_topic={}
        topic_counts={}
        for entry in self.entries:
            total_topic[entry.topic]=(total_topic.get(entry.topic,0)+entry.confidence)
            topic_counts[entry.topic]=(topic_counts.get(entry.topic,0)+1)
        print(f"total hours:{total_hours}")
        print("Average confidence per topic:")
        for topic in total_topic:
            average=total_topic[topic]/topic_counts[topic]
            print(f"{topic}:{average}")

if __name__=="__main__":
    log = StudyLog("study_log.json")
    '''log.add_entry("2026-07-14", "classes", 90, 4, "went well")
    log.add_entry("2026-07-15", "classes", 60, 5, "good session")
    log.add_entry("2026-07-15", "pytorch", 120, 3, "learned Dataset")'''

    log.summary()