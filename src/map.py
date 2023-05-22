from dataclasses import dataclass
import pygame, pytmx, pyscroll

@dataclass
class Portal : 
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str


@dataclass
class Map : 
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals : list[Portal]

class MapManager : 
    def __init__(self,screen,player):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.current_map = "house"
        self.register_map("world",portals=[
            Portal(from_world = "world",origin_point ="enter_house",target_world ="house",teleport_point ="spawn_house"),
            Portal(from_world = "world",origin_point ="enter_church",target_world ="church",teleport_point ="spawn_church"),
            Portal(from_world = "world",origin_point ="enter_market",target_world ="market",teleport_point ="spawn_market"),
            Portal(from_world = "world",origin_point ="enter_city_hall",target_world ="city_hall",teleport_point ="spawn_city_hall"),
            Portal(from_world = "world",origin_point ="enter_theatre",target_world ="theatre",teleport_point ="spawn_theatre"),
            Portal(from_world = "world",origin_point ="enter_courthouse",target_world ="courthouse",teleport_point ="spawn_courthouse")
        ])
        self.register_map("house",portals=[
            Portal(from_world = "house",origin_point ="exit_house",target_world ="world",teleport_point ="enter_house_exit")
        ])
        self.register_map("church",portals=[
            Portal(from_world = "church",origin_point ="exit_church",target_world ="world",teleport_point ="enter_church_exit")
        ])
        self.register_map("market",portals=[
            Portal(from_world = "market",origin_point ="exit_market",target_world ="world",teleport_point ="enter_market_exit")
        ])
        self.register_map("city_hall",portals=[
            Portal(from_world = "city_hall",origin_point ="exit_city_hall",target_world ="world",teleport_point ="enter_city_hall_exit")
        ])
        self.register_map("theatre",portals=[
            Portal(from_world = "theatre",origin_point ="exit_theatre",target_world ="world",teleport_point ="enter_theatre_exit")
        ])
        self.register_map("courthouse",portals=[
            Portal(from_world = "courthouse",origin_point ="exit_courthouse",target_world ="world",teleport_point ="enter_courthouse_exit")
        ])
        self.teleport_player('player')
        
    def register_map(self,name,portals=[]):
        #Load and draw the map
        tmx_data = pytmx.util_pygame.load_pygame(f"assets/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1
        
        #Creation of the collision list
        walls = []
        for obj in tmx_data.objects : 
            if obj.name == "collision" :
                walls.append(pygame.Rect(obj.x,obj.y,obj.width,obj.height))
        
        #Manage the layer group
        group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer = 4)
        group.add(self.player)
        #Create a map object
        self.maps[name] = Map(name,walls,group,tmx_data,portals)
    #Recover a map    
    def get_map(self): return self.maps[self.current_map]
    
    #Recover a group
    def get_group(self): return self.get_map().group
    
    #Recover walls
    def get_walls(self): return self.get_map().walls
    
    #Recover an object
    def get_obect(self,name): return self.get_map().tmx_data.get_object_by_name(name)
    
    #Check collisions and portals
    def check_collision(self):
        #Portals
        for portal in self.get_map().portals :
            if portal.from_world == self.current_map : 
                point = self.get_obect(portal.origin_point)
                rect = pygame.Rect(point.x,point.y,point.width,point.height)
                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)
                    
        #collisions
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) >-1 : 
                sprite.move_back()
    
    #Teleport the player to his spawnpoint
    def teleport_player(self,name):
        point =self.get_obect(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()
    
    #Draw and center the map on the player
    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)
    
    #Update the game    
    def update(self):
        self.get_group().update()
        self.check_collision()