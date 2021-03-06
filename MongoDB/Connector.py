import sys
import pymongo
import os
sys.path.append("..")

class Connector():
    def __init__(self):
        self.client = pymongo.MongoClient(os.environ["MongoDB_CONNECTION_STRING"]).HutAssistant

    def get_leaderboard(self) -> list:
        return list(self.client.UserProfiles.find().sort('Games Won', pymongo.DESCENDING).limit(10))

    def get_profile(self, user_id) -> dict:
        try:
            return dict(self.client.UserProfiles.find_one({"_id" : user_id}, {'_id' : False}))
        except Exception:
            return None

    def get_profile_count(self) -> int:
        return self.client.UserProfiles.find().count()

    def get_all_matches_count(self) -> int:
        return self.client.GladiatorGameMessages.find().count()
        
    def get_all_match_messages(self, user_id):
        return list(self.client.GladiatorGameMessages.find({"Players" : f"<@{user_id}>"}, {'_id' : False}).sort('Date', pymongo.DESCENDING).limit(10))

    def get_attack_information(self) -> list:
        return list(self.client.AttackInformation.find({}, {'_id': False}))

    def get_damage_types(self) -> list:
        return list(self.client.DamageTypes.find({}, {'_id': False}))

    def get_turn_debuffs(self) -> list:
        return list(self.client.TurnDebuffs.find({}, {'_id': False}))

    def get_npcs(self) -> list:
        return list(self.client.NPCs.find({}, {'_id': False}))

    def get_npcs_spawn_settings(self) -> list:
        return list(self.client.NPCSpawnSettings.find({}, {'_id': False}))

    def get_gladiator_game_settings(self) -> dict:
        game_settings = self.client.GladiatorGameSettings.find_one() 
        game_settings.pop("_id")
        return game_settings

    def get_events(self) -> list:
        return list(self.client.Events.find({}, {'_id': False}))

    def get_equipments(self) -> list:
        return list(self.client.Equipments.find({}, {'_id': False}))

    def get_equipment_slots(self) -> list:
        return list(self.client.EquipmentSlots.find({}, {'_id': False}))

    def get_guild_settings(self) -> dict:
        guild_settings = self.client.GuildSettings.find_one() 
        guild_settings.pop("_id")
        return guild_settings

    def insert_suggestion(self, suggestion_dict):
        self.client.BotSuggestions.insert_one(suggestion_dict)    
    
    def insert_usermade_npc(self, npc_dict):
        self.client.UserNPCs.insert_one(npc_dict)