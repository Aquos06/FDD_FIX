import cv2

class calculate:
    def __init__(self):
        self.inside_id = []
        self.final_coordinates = []
        
    def find(self, region, coordinates):
        self.coordinates = coordinates
        gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
        # canny = cv2.Canny(gray, 120, 255, 1)
        self.xyxy2xywh()
        
        cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            inside = cv2.pointPolygonTest(c, (self.final_coordinates[0],self.final_coordinates[1]), False)
            if int(inside) > 0:
                return 1
                
    def xyxy2xywh(self):
        self.final_coordinates.clear()
        self.final_coordinates.append((self.coordinates[1] + self.coordinates[3]) / 2)  # x center
        self.final_coordinates.append((self.coordinates[2] + self.coordinates[4]) / 2)  # y center