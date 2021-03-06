import requests
import json


class ClubhouseAPI:

    def __init__(self, user):
        self.api_url = 'https://www.clubhouseapi.com/api'
        self.user = user

    def me(self):
        return requests.post('{}/me'.format(self.api_url), headers=self.user.headers, cookies=self.user.cookies)

    def get_profile(self, user_id):
        return requests.post('{}/get_profile'.format(self.api_url), json={'user_id': user_id},
                             headers=self.user.headers, cookies=self.user.cookies)

    def get_followers(self, user_id, page_size=50, page=1):
        return requests.get(
            '{}/get_followers?user_id={}&page_size={}&page={}'.format(self.api_url, user_id, page_size, page),
            headers=self.user.headers, cookies=self.user.cookies)

    def get_following(self, user_id, page_size=50, page=1):
        return requests.get(
            '{}/get_following?user_id={}&page_size={}&page={}'.format(self.api_url, user_id, page_size, page),
            headers=self.user.headers, cookies=self.user.cookies)

    def get_all_topics(self):
        return requests.get('{}/get_all_topics'.format(self.api_url),
                             headers=self.user.headers, cookies=self.user.cookies)

    def get_users_for_topic(self, topic_id, page_size=25, page=1):
        return requests.get(
            '{}/get_users_for_topic?topic_id={}&page_size={}&page={}'.format(self.api_url, topic_id, page_size, page),
            headers=self.user.headers, cookies=self.user.cookies)

    def get_clubs_for_topic(self, topic_id, page_size=25, page=1):
        return requests.get(
            '{}/get_clubs_for_topic?topic_id={}&page_size={}&page={}'.format(self.api_url, topic_id, page_size, page),
            headers=self.user.headers, cookies=self.user.cookies)

    def get_club(self, club_id):
        return requests.post('{}/get_club'.format(self.api_url), json={'club_id': club_id, 'source_topic_id': None},
                             headers=self.user.headers, cookies=self.user.cookies)

    def get_club_members(self, club_id, return_followers=1, return_members=0, page_size=50, page=1):
        return requests.get(
            '{}/get_club_members?club_id={}&return_followers={}&return_members={}&page_size={}&page={}'.format(
                self.api_url, club_id, return_followers, return_members, page_size, page),
            headers=self.user.headers, cookies=self.user.cookies)

    def check_for_update(self, is_testflight=0):
        return requests.get(
            '{}/check_for_update?is_testflight={}'.format(self.api_url, is_testflight),
            headers=self.user.headers, cookies=self.user.cookies)

    def get_suggested_invites(self, phone_numbers):
        contacts = []
        for number in phone_numbers:
            contacts.append({'phone_number': number})
        return requests.post(
            '{}/get_suggested_invites'.format(self.api_url), json={'club_id': None, 'contacts': contacts, 'upload_contacts': False},
            headers=self.user.headers, cookies=self.user.cookies)

    def get_events(self, is_filtered='false', page_size=25, page=1):
        return requests.get(
            '{}/get_events?is_filtered={}&page_size={}&page={}'.format(self.api_url, is_filtered, page_size, page),
            headers=self.user.headers, cookies=self.user.cookies)

    def search_users(self, query):
        return requests.post('{}/search_users'.format(self.api_url), json={'cofollows_only': False,
                             'followers_only': False, 'following_only': False, 'query': query},
                             headers=self.user.headers, cookies=self.user.cookies)

    def search_clubs(self, query):
        return requests.post('{}/search_clubs'.format(self.api_url), json={'cofollows_only': False,
                             'followers_only': False, 'following_only': False, 'query': query},
                             headers=self.user.headers, cookies=self.user.cookies)


class User:
    def __init__(self, token, user_id, user_agent, device_id, cookie_uid):
        self.token = token
        self.user_id = user_id
        self.user_agent = user_agent
        self.device_id = device_id
        self.cookie_uid = cookie_uid
        self.headers = self.set_headers()
        self.cookies = self.set_cookies()

    def set_headers(self):
        headers = {}
        headers.update({'Authorization': self.token})
        headers.update({'CH-Languages': 'en-US'})
        headers.update({'CH-UserID': self.user_id})
        headers.update({'CH-Locale': 'en_US'})
        headers.update({'Accept-Encoding': 'gzip, deflate, br'})
        headers.update({'Accept-Language': 'en-US;q=1'})
        headers.update({'CH-AppBuild': '269'})
        headers.update({'CH-AppVersion': '0.1.25'})
        headers.update({'Accept': 'application/json'})
        headers.update({'CH-DeviceId': self.device_id})
        headers.update({'User-Agent': self.user_agent})
        headers.update({'Connection': 'keep-alive'})
        return headers

    def set_cookies(self):
        cookies = {'__cfduid': self.cookie_uid}
        return cookies


user = User(token='Token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', user_id='XXXXXXXXXX', user_agent='clubhouse/XXX (iXXXXX; iOS XX.X.X)',
            device_id='XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX', cookie_uid='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

api = ClubhouseAPI(user)

resp = api.search_users('.').text
print(resp)
print(f"Number of Clubhouse users: {json.loads(resp)['count']:,}")


'''
All endpoints:


record_action_trails
 start_phone_number_auth 
call_phone_number_auth 
resend_phone_number_auth 
complete_phone_number_auth
 check_waitlist_status 
get_release_notes
 get_all_topics 
get_topic 
get_clubs_for_topic
 get_users_for_topic 
update_name 
update_display
name 
update_bio
 update_username
 update_twitter_username
 update_skintone
add_user_topic 
remove_user_topic
 update_notifications
 add_email 
get_settings 
update_instagram_username 
report_incident 
get_followers 
get_following 
get_mutual_follows
 get_suggested_follows_friends_only 
get_suggested_follows_all 
get_suggested_follows_similar
 ignore_suggested_follow
 follow
 follow_multiple 
unfollow
 update_follow_notifications
 block 
unblock
 get_profile
 get_channel 
get_channels 
get_suggested_speakers
 create_channel 
active_ping 
invite_to_existing_channel 
audience_reply 
block_from_channel 
get_welcome_channel 
get_create_channel_targets
 update_channel_flags
 hide_channel 
get_notifications
 get_actionable_notifications
 ignore_actionable_notification
 me 
get_online_friends
 search_users 
search_clubs
 check_for_update 
get_suggested_invites
 invite_to_app
 invite_from_waitlist 
add_club_admin
 add_club_member 
get_club 
get_club_members 
get_suggested_club_invites
 remove_club_admin 
remove_club_member 
accept_club_member_invite
 follow_club 
unfollow_club 
get_club_nominations 
approve_club_nomination
 reject_club_nomination
get_clubs 
update_is_follow_allowed 
update_is_membership_private 
update_is_community
 update_club_description
 update_club_rules 
update_club_topics 
update_club_photo
add_club_topic 
remove_club_topic 
get_events
 get_events_for_user 
get_events_to_start 
delete_event
create_event
 edit_event 
get_event
'''
