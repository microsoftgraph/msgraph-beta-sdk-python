from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group, printer, printer_base, printer_share_viewpoint, user

from . import printer_base

class PrinterShare(printer_base.PrinterBase):
    def __init__(self,) -> None:
        """
        Instantiates a new PrinterShare and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.printerShare"
        # If true, all users and groups will be granted access to this printer share. This supersedes the allow lists defined by the allowedUsers and allowedGroups navigation properties.
        self._allow_all_users: Optional[bool] = None
        # The groups whose users have access to print using the printer.
        self._allowed_groups: Optional[List[group.Group]] = None
        # The users who have access to print using the printer.
        self._allowed_users: Optional[List[user.User]] = None
        # The DateTimeOffset when the printer share was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The printer that this printer share is related to.
        self._printer: Optional[printer.Printer] = None
        # Additional data for a printer share as viewed by the signed-in user.
        self._view_point: Optional[printer_share_viewpoint.PrinterShareViewpoint] = None
    
    @property
    def allow_all_users(self,) -> Optional[bool]:
        """
        Gets the allowAllUsers property value. If true, all users and groups will be granted access to this printer share. This supersedes the allow lists defined by the allowedUsers and allowedGroups navigation properties.
        Returns: Optional[bool]
        """
        return self._allow_all_users
    
    @allow_all_users.setter
    def allow_all_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAllUsers property value. If true, all users and groups will be granted access to this printer share. This supersedes the allow lists defined by the allowedUsers and allowedGroups navigation properties.
        Args:
            value: Value to set for the allow_all_users property.
        """
        self._allow_all_users = value
    
    @property
    def allowed_groups(self,) -> Optional[List[group.Group]]:
        """
        Gets the allowedGroups property value. The groups whose users have access to print using the printer.
        Returns: Optional[List[group.Group]]
        """
        return self._allowed_groups
    
    @allowed_groups.setter
    def allowed_groups(self,value: Optional[List[group.Group]] = None) -> None:
        """
        Sets the allowedGroups property value. The groups whose users have access to print using the printer.
        Args:
            value: Value to set for the allowed_groups property.
        """
        self._allowed_groups = value
    
    @property
    def allowed_users(self,) -> Optional[List[user.User]]:
        """
        Gets the allowedUsers property value. The users who have access to print using the printer.
        Returns: Optional[List[user.User]]
        """
        return self._allowed_users
    
    @allowed_users.setter
    def allowed_users(self,value: Optional[List[user.User]] = None) -> None:
        """
        Sets the allowedUsers property value. The users who have access to print using the printer.
        Args:
            value: Value to set for the allowed_users property.
        """
        self._allowed_users = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The DateTimeOffset when the printer share was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The DateTimeOffset when the printer share was created. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterShare:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterShare
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterShare()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import group, printer, printer_base, printer_share_viewpoint, user

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedGroups": lambda n : setattr(self, 'allowed_groups', n.get_collection_of_object_values(group.Group)),
            "allowedUsers": lambda n : setattr(self, 'allowed_users', n.get_collection_of_object_values(user.User)),
            "allowAllUsers": lambda n : setattr(self, 'allow_all_users', n.get_bool_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "printer": lambda n : setattr(self, 'printer', n.get_object_value(printer.Printer)),
            "viewPoint": lambda n : setattr(self, 'view_point', n.get_object_value(printer_share_viewpoint.PrinterShareViewpoint)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def printer(self,) -> Optional[printer.Printer]:
        """
        Gets the printer property value. The printer that this printer share is related to.
        Returns: Optional[printer.Printer]
        """
        return self._printer
    
    @printer.setter
    def printer(self,value: Optional[printer.Printer] = None) -> None:
        """
        Sets the printer property value. The printer that this printer share is related to.
        Args:
            value: Value to set for the printer property.
        """
        self._printer = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("allowedGroups", self.allowed_groups)
        writer.write_collection_of_object_values("allowedUsers", self.allowed_users)
        writer.write_bool_value("allowAllUsers", self.allow_all_users)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("printer", self.printer)
        writer.write_object_value("viewPoint", self.view_point)
    
    @property
    def view_point(self,) -> Optional[printer_share_viewpoint.PrinterShareViewpoint]:
        """
        Gets the viewPoint property value. Additional data for a printer share as viewed by the signed-in user.
        Returns: Optional[printer_share_viewpoint.PrinterShareViewpoint]
        """
        return self._view_point
    
    @view_point.setter
    def view_point(self,value: Optional[printer_share_viewpoint.PrinterShareViewpoint] = None) -> None:
        """
        Sets the viewPoint property value. Additional data for a printer share as viewed by the signed-in user.
        Args:
            value: Value to set for the view_point property.
        """
        self._view_point = value
    

