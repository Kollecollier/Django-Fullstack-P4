from django import template

register = template.Library()


@register.filter(name="is_following")
def is_following(current_user, user):
    following_list = current_user.following.all()
    return following_list.filter(following=user).exists()
