"""
Acunu Python Bindings;

Submodule            Function
=========            ======================================================
castle               To interact with Castle; this module provides the most
                     commonly used interfaces to exchange data with Castle,
                     performing versioning operations, and some control
                     parameters (such as setting checkpoint frequency).

libcastle            This is a SWIG generated layer that talks directly to
                     the C libcastle; not recommended for normal use cases,
                     the castle module is built on top of this, and should
                     provide all the control most users need.
"""
__all__ = ["castle"]
