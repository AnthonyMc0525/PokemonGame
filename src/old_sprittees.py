def update(self, event):
    # self.vx=0
    if event.type== pygame.KEYDOWN:
            # Max right: 538
            # Max left: 3
            # Max up: -1
            # Max Down: 529

        if event.key== pygame.K_LEFT or event.key == pygame.K_a:
            if self.rect.x > MAX_LEFT and self.rect.x <= MAX_RIGHT:
                self.dir="left"
                # self.vx -= self.speed
                self.rect.x -= self.speed
                self.index+= 1
                if self.index >= len(self.imagesleft):
                    self.index=0
                self.image= pygame.transform.flip(self.imagesleft[self.index], True, False)

        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if self.rect.x >= MAX_LEFT and self.rect.x < MAX_RIGHT:
                self.dir="right"
                # self.vx += self.speed
                self.rect.x += self.speed
                self.index+= 1
                if self.index >= len(self.imagesright):
                    self.index=0
                self.image=self.imagesright[self.index]

        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            if self.rect.y > MAX_UP and self.rect.y <= MAX_DOWN:
                self.dir="up"
                # self.rect.y -= self.speed
                self.rect.y -= self.speed
                self.index+= 1
                if self.index >= len(self.imagesup):
                    self.index=0
                self.image=self.imagesup[self.index]
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if self.rect.y >= MAX_UP and self.rect.y < MAX_DOWN:
                self.dir="down"
                # self.rect.y += self.speed
                self.rect.y += self.speed
                self.index+= 1
                if self.index >= len(self.imagesdown):
                    self.index=0
                self.image=self.imagesdown[self.index]
