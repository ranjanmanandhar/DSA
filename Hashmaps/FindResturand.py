from typing import List 

class LeastIndex:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        result = []
        current_sum = float()
        
        index_map = {restaurant: index for index, restaurant in enumerate(list1)}
        for index, resturant in enumerate(list2):
            if resturant in index_map:
                current_sum = index + index_map[resturant]
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [resturant]
                elif current_sum == min_sum:
                    result.append(resturant)
        
        return result
    
a = LeastIndex()

t = a.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
print(t)