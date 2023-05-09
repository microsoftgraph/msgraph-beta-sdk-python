from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class PrivilegedRoleSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedRoleSettings and sets the default values.
        """
        super().__init__()
        # The approvalOnElevation property
        self._approval_on_elevation: Optional[bool] = None
        # The approverIds property
        self._approver_ids: Optional[List[str]] = None
        # The elevationDuration property
        self._elevation_duration: Optional[timedelta] = None
        # The isMfaOnElevationConfigurable property
        self._is_mfa_on_elevation_configurable: Optional[bool] = None
        # The lastGlobalAdmin property
        self._last_global_admin: Optional[bool] = None
        # The maxElavationDuration property
        self._max_elavation_duration: Optional[timedelta] = None
        # The mfaOnElevation property
        self._mfa_on_elevation: Optional[bool] = None
        # The minElevationDuration property
        self._min_elevation_duration: Optional[timedelta] = None
        # The notificationToUserOnElevation property
        self._notification_to_user_on_elevation: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ticketingInfoOnElevation property
        self._ticketing_info_on_elevation: Optional[bool] = None
    
    @property
    def approval_on_elevation(self,) -> Optional[bool]:
        """
        Gets the approvalOnElevation property value. The approvalOnElevation property
        Returns: Optional[bool]
        """
        return self._approval_on_elevation
    
    @approval_on_elevation.setter
    def approval_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the approvalOnElevation property value. The approvalOnElevation property
        Args:
            value: Value to set for the approval_on_elevation property.
        """
        self._approval_on_elevation = value
    
    @property
    def approver_ids(self,) -> Optional[List[str]]:
        """
        Gets the approverIds property value. The approverIds property
        Returns: Optional[List[str]]
        """
        return self._approver_ids
    
    @approver_ids.setter
    def approver_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the approverIds property value. The approverIds property
        Args:
            value: Value to set for the approver_ids property.
        """
        self._approver_ids = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedRoleSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedRoleSettings()
    
    @property
    def elevation_duration(self,) -> Optional[timedelta]:
        """
        Gets the elevationDuration property value. The elevationDuration property
        Returns: Optional[timedelta]
        """
        return self._elevation_duration
    
    @elevation_duration.setter
    def elevation_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the elevationDuration property value. The elevationDuration property
        Args:
            value: Value to set for the elevation_duration property.
        """
        self._elevation_duration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "approvalOnElevation": lambda n : setattr(self, 'approval_on_elevation', n.get_bool_value()),
            "approverIds": lambda n : setattr(self, 'approver_ids', n.get_collection_of_primitive_values(str)),
            "elevationDuration": lambda n : setattr(self, 'elevation_duration', n.get_timedelta_value()),
            "isMfaOnElevationConfigurable": lambda n : setattr(self, 'is_mfa_on_elevation_configurable', n.get_bool_value()),
            "lastGlobalAdmin": lambda n : setattr(self, 'last_global_admin', n.get_bool_value()),
            "maxElavationDuration": lambda n : setattr(self, 'max_elavation_duration', n.get_timedelta_value()),
            "mfaOnElevation": lambda n : setattr(self, 'mfa_on_elevation', n.get_bool_value()),
            "minElevationDuration": lambda n : setattr(self, 'min_elevation_duration', n.get_timedelta_value()),
            "notificationToUserOnElevation": lambda n : setattr(self, 'notification_to_user_on_elevation', n.get_bool_value()),
            "ticketingInfoOnElevation": lambda n : setattr(self, 'ticketing_info_on_elevation', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_mfa_on_elevation_configurable(self,) -> Optional[bool]:
        """
        Gets the isMfaOnElevationConfigurable property value. The isMfaOnElevationConfigurable property
        Returns: Optional[bool]
        """
        return self._is_mfa_on_elevation_configurable
    
    @is_mfa_on_elevation_configurable.setter
    def is_mfa_on_elevation_configurable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMfaOnElevationConfigurable property value. The isMfaOnElevationConfigurable property
        Args:
            value: Value to set for the is_mfa_on_elevation_configurable property.
        """
        self._is_mfa_on_elevation_configurable = value
    
    @property
    def last_global_admin(self,) -> Optional[bool]:
        """
        Gets the lastGlobalAdmin property value. The lastGlobalAdmin property
        Returns: Optional[bool]
        """
        return self._last_global_admin
    
    @last_global_admin.setter
    def last_global_admin(self,value: Optional[bool] = None) -> None:
        """
        Sets the lastGlobalAdmin property value. The lastGlobalAdmin property
        Args:
            value: Value to set for the last_global_admin property.
        """
        self._last_global_admin = value
    
    @property
    def max_elavation_duration(self,) -> Optional[timedelta]:
        """
        Gets the maxElavationDuration property value. The maxElavationDuration property
        Returns: Optional[timedelta]
        """
        return self._max_elavation_duration
    
    @max_elavation_duration.setter
    def max_elavation_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the maxElavationDuration property value. The maxElavationDuration property
        Args:
            value: Value to set for the max_elavation_duration property.
        """
        self._max_elavation_duration = value
    
    @property
    def mfa_on_elevation(self,) -> Optional[bool]:
        """
        Gets the mfaOnElevation property value. The mfaOnElevation property
        Returns: Optional[bool]
        """
        return self._mfa_on_elevation
    
    @mfa_on_elevation.setter
    def mfa_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the mfaOnElevation property value. The mfaOnElevation property
        Args:
            value: Value to set for the mfa_on_elevation property.
        """
        self._mfa_on_elevation = value
    
    @property
    def min_elevation_duration(self,) -> Optional[timedelta]:
        """
        Gets the minElevationDuration property value. The minElevationDuration property
        Returns: Optional[timedelta]
        """
        return self._min_elevation_duration
    
    @min_elevation_duration.setter
    def min_elevation_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the minElevationDuration property value. The minElevationDuration property
        Args:
            value: Value to set for the min_elevation_duration property.
        """
        self._min_elevation_duration = value
    
    @property
    def notification_to_user_on_elevation(self,) -> Optional[bool]:
        """
        Gets the notificationToUserOnElevation property value. The notificationToUserOnElevation property
        Returns: Optional[bool]
        """
        return self._notification_to_user_on_elevation
    
    @notification_to_user_on_elevation.setter
    def notification_to_user_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the notificationToUserOnElevation property value. The notificationToUserOnElevation property
        Args:
            value: Value to set for the notification_to_user_on_elevation property.
        """
        self._notification_to_user_on_elevation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("approvalOnElevation", self.approval_on_elevation)
        writer.write_collection_of_primitive_values("approverIds", self.approver_ids)
        writer.write_timedelta_value("elevationDuration", self.elevation_duration)
        writer.write_bool_value("isMfaOnElevationConfigurable", self.is_mfa_on_elevation_configurable)
        writer.write_bool_value("lastGlobalAdmin", self.last_global_admin)
        writer.write_timedelta_value("maxElavationDuration", self.max_elavation_duration)
        writer.write_bool_value("mfaOnElevation", self.mfa_on_elevation)
        writer.write_timedelta_value("minElevationDuration", self.min_elevation_duration)
        writer.write_bool_value("notificationToUserOnElevation", self.notification_to_user_on_elevation)
        writer.write_bool_value("ticketingInfoOnElevation", self.ticketing_info_on_elevation)
    
    @property
    def ticketing_info_on_elevation(self,) -> Optional[bool]:
        """
        Gets the ticketingInfoOnElevation property value. The ticketingInfoOnElevation property
        Returns: Optional[bool]
        """
        return self._ticketing_info_on_elevation
    
    @ticketing_info_on_elevation.setter
    def ticketing_info_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the ticketingInfoOnElevation property value. The ticketingInfoOnElevation property
        Args:
            value: Value to set for the ticketing_info_on_elevation property.
        """
        self._ticketing_info_on_elevation = value
    

