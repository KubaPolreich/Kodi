import xbmcplugin
import xbmcgui
import xbmcaddon
import sys

addon = xbmcaddon.Addon()
api_token = addon.getSetting("api_token")
handle = int(sys.argv[1])

if not api_token:
    xbmcgui.Dialog().notification("Webshare", "API token není nastaven", xbmcgui.NOTIFICATION_ERROR)
    xbmcplugin.endOfDirectory(handle)
else:
    list_item = xbmcgui.ListItem(label="Testovací video")
    url = "https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_10mb.mp4"
    list_item.setPath(url)
    list_item.setProperty("IsPlayable", "true")
    xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=list_item, isFolder=False)
    xbmcplugin.endOfDirectory(handle)
