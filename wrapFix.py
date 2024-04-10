def wrap_position(position, screen_rect):
   
        if position.x < screen_rect.left:
            position.x = screen_rect.right
        elif position.x > screen_rect.right:
            position.x = screen_rect.left
        if position.y < screen_rect.top:
            position.y = screen_rect.bottom
        elif position.y > screen_rect.bottom:
            position.y = screen_rect.top
        return position