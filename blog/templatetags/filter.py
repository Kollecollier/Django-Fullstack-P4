from django import template

register = template.Library()


@register.filter(name="has_commented")
def has_commented(post, user):
    return post.comments.filter(user=user).exists()

@register.filter(name="is_comment_owner")
def is_comment_owner(comment, user):
    return comment.user == user