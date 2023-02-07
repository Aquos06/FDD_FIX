import cv2

class calculate:
    def __init__(self):
        self.inside_id = []
        self.final_coordinates = []
        
    def find(self, region, coordinates, person = False):
        self.coordinates = coordinates
        gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
        
        if not person:
            self.xyxy2xywh()
        else:
            self.xyxy2xywhPerson()

        cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for cnt in cnts:
            inside = cv2.pointPolygonTest(cnt, (self.final_coordinates[0],self.final_coordinates[1]), False)
            if int(inside) > 0:
                return 1
        return 0
                
    def xyxy2xywh(self):
        self.final_coordinates.clear()
        self.final_coordinates.append((self.coordinates[1] + self.coordinates[3]) / 2)  # x center
        self.final_coordinates.append((self.coordinates[2] + self.coordinates[4]) / 2)  # y center

    def xyxy2xywhPerson(self):
        self.final_coordinates.clear()
        self.final_coordinates.append((self.coordinates[0] + self.coordinates[2]) / 2)  # x center
        self.final_coordinates.append((self.coordinates[1] + self.coordinates[3]) / 2)  # y center

def main():
    cal = calculate()
    img = cv2.imread('./ROI/Camera1/fall_down.jpg')

    print(cal.find(img,[0,400,400,800,800]))
    cv2.circle(img,(600,600),3,(0,255,0),-1)

    cv2.imshow('img', img)
    cv2.waitKey()

if __name__ == "__main__":
    main()

