import html

def org_rep(org):
    ans = html.unescape(org)
    if org != ans:
        print(f'{org} is unescaped to {ans}')
    return ans


if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kaogaii2.settings')
    django.setup()
    from app.models import Creator, Avatar, Item

    for avatar in Avatar.objects.all():
        ans_name = avatar.avatar_name
        ans_name = org_rep(ans_name)
        avatar.avatar_name = ans_name
        avatar.save()

    for item in Item.objects.all():
        ans_name = item.item_name
        ans_name = org_rep(ans_name)
        item.item_name = ans_name
        item.save()

    for creator in Creator.objects.all():
        ans_name = creator.creator_name
        ans_name = org_rep(ans_name)
        creator.creator_name = ans_name
        creator.save()
