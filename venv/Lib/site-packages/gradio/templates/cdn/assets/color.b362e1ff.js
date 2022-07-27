import { ae as ordered_colors } from './index.8ea4571f.js';

const get_next_color = (index) => {
  return ordered_colors[index % ordered_colors.length];
};

export { get_next_color as g };
