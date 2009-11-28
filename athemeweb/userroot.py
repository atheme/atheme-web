#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from middleware.classpublisher import webinfo
from thirdparty.templite import Templite
from middleware.athemeconnection import AthemeXMLConnection
from athemeweb.config import XMLRPC_PATH

from urllib import quote_plus

def get_xmlrpc_connection():
    sessiondata = webinfo.environ['paste.session.factory']()
    conn = AthemeXMLConnection(XMLRPC_PATH)
    conn.username = sessiondata['conn.username']
    conn.authcookie = sessiondata['conn.authcookie']

    return conn

class ChannelRoot(object):
    def list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('mychannels_list')
        return t.render(webinfo=webinfo, conn=conn)

    def info(self, channel):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('channelinfo')
        return t.render(webinfo=webinfo, conn=conn, channel=channel)

    def edit_flags(self, channel, nick=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('channeleditflags')
        return t.render(webinfo=webinfo, conn=conn, channel=channel, nick=nick)

    def set_flags(self, channel, nick, flags):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.chanserv.set_access_flags(channel, nick, flags)
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'info?channel=' + quote_plus(channel)
        return ''

    def remove_flags(self, channel, nick):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.chanserv.set_access_flags(channel, nick, '-*fF')
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'info?channel=' + quote_plus(channel)
        return ''

    def info(self, channel):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('channelinfo')
        return t.render(webinfo=webinfo, conn=conn, channel=channel)

class MemoRoot(object):
    def delete_confirm(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.delete(id)
        t = Templite('memodeleted')
        return t.render(webinfo=webinfo, conn=conn, id=id)

    def delete(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('memodelete')
        return t.render(webinfo=webinfo, conn=conn, id=id)

    def read(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('memoread')
        return t.render(webinfo=webinfo, conn=conn, id=id)

    def list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('memolist')
        return t.render(webinfo=webinfo, conn=conn)

    def ignore_list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('memoignores')
        return t.render(webinfo=webinfo, conn=conn)

    def ignore_add(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('memoignoreadd')
        return t.render(webinfo=webinfo, conn=conn)

    def ignore_add_commit(self, account):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.ignore_add(account)
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'ignore_list'
        return ''

    def ignore_delete(self, account):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.ignore_delete(account)
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'ignore_list'
        return ''

    def ignore_clear(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.ignore_clear()
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'ignore_list'
        return ''

    def write(self, to=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('memowrite')
        return t.render(webinfo=webinfo, conn=conn, to=to)        

    def write_commit(self, to, message):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.send(to, message)
        t = Templite('memosent')
        return t.render(webinfo=webinfo, conn=conn, to=to)

    def forward(self, id, to=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        t = Templite('memoforward')
        return t.render(webinfo=webinfo, conn=conn, message_id=id, to=to)

    def forward_commit(self, to, message_id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.forward(to, message_id)
        t = Templite('memosent')
        return t.render(webinfo=webinfo, conn=conn, to=to)

class UserRoot(object):
    def __init__(self):
        self.memo = MemoRoot()
        self.channel = ChannelRoot()

    def login(self):
        t = Templite('userlogin')
        return t.render()

    def process_login(self, nickname, password):
        webinfo.response.status = "302 Found"
        try:
            conn = AthemeXMLConnection(XMLRPC_PATH)
            conn.login(nickname, password)
        except:
            webinfo.response.headers['location'] = 'login'
            return ''

        webinfo.response.headers['location'] = 'dashboard'
        sessiondata = webinfo.environ['paste.session.factory']()
        sessiondata['conn.username'] = conn.username
        sessiondata['conn.authcookie'] = conn.authcookie
        return ''

    def dashboard(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        t = Templite('dashboard')
        return t.render(webinfo=webinfo, conn=conn)

    def logout(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        conn.logout()
        sessiondata = webinfo.environ['paste.session.factory']()
        del sessiondata['conn.username']
        del sessiondata['conn.authcookie']

        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'login'
        return ''