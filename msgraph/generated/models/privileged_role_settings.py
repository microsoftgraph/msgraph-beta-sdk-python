from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class PrivilegedRoleSettings(entity.Entity):
    @property
    def approval_on_elevation(self,) -> Optional[bool]:
        """
        Gets the approvalOnElevation property value. true if the approval is required when activate the role. false if the approval is not required when activate the role.
        Returns: Optional[bool]
        """
        return self._approval_on_elevation
    
    @approval_on_elevation.setter
    def approval_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the approvalOnElevation property value. true if the approval is required when activate the role. false if the approval is not required when activate the role.
        Args:
            value: Value to set for the approvalOnElevation property.
        """
        self._approval_on_elevation = value
    
    @property
    def approver_ids(self,) -> Optional[List[str]]:
        """
        Gets the approverIds property value. List of Approval ids, if approval is required for activation.
        Returns: Optional[List[str]]
        """
        return self._approver_ids
    
    @approver_ids.setter
    def approver_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the approverIds property value. List of Approval ids, if approval is required for activation.
        Args:
            value: Value to set for the approverIds property.
        """
        self._approver_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedRoleSettings and sets the default values.
        """
        super().__init__()
        # true if the approval is required when activate the role. false if the approval is not required when activate the role.
        self._approval_on_elevation: Optional[bool] = None
        # List of Approval ids, if approval is required for activation.
        self._approver_ids: Optional[List[str]] = None
        # The duration when the role is activated.
        self._elevation_duration: Optional[Timedelta] = None
        # true if mfaOnElevation is configurable. false if mfaOnElevation is not configurable.
        self._is_mfa_on_elevation_configurable: Optional[bool] = None
        # Internal used only.
        self._last_global_admin: Optional[bool] = None
        # Maximal duration for the activated role.
        self._max_elavation_duration: Optional[Timedelta] = None
        # true if MFA is required to activate the role. false if MFA is not required to activate the role.
        self._mfa_on_elevation: Optional[bool] = None
        # Minimal duration for the activated role.
        self._min_elevation_duration: Optional[Timedelta] = None
        # true if send notification to the end user when the role is activated. false if do not send notification when the role is activated.
        self._notification_to_user_on_elevation: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # true if the ticketing information is required when activate the role. false if the ticketing information is not required when activate the role.
        self._ticketing_info_on_elevation: Optional[bool] = None
    
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
    def elevation_duration(self,) -> Optional[Timedelta]:
        """
        Gets the elevationDuration property value. The duration when the role is activated.
        Returns: Optional[Timedelta]
        """
        return self._elevation_duration
    
    @elevation_duration.setter
    def elevation_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the elevationDuration property value. The duration when the role is activated.
        Args:
            value: Value to set for the elevationDuration property.
        """
        self._elevation_duration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "approval_on_elevation": lambda n : setattr(self, 'approval_on_elevation', n.get_bool_value()),
            "approver_ids": lambda n : setattr(self, 'approver_ids', n.get_collection_of_primitive_values(str)),
            "elevation_duration": lambda n : setattr(self, 'elevation_duration', n.get_object_value(Timedelta)),
            "is_mfa_on_elevation_configurable": lambda n : setattr(self, 'is_mfa_on_elevation_configurable', n.get_bool_value()),
            "last_global_admin": lambda n : setattr(self, 'last_global_admin', n.get_bool_value()),
            "max_elavation_duration": lambda n : setattr(self, 'max_elavation_duration', n.get_object_value(Timedelta)),
            "mfa_on_elevation": lambda n : setattr(self, 'mfa_on_elevation', n.get_bool_value()),
            "min_elevation_duration": lambda n : setattr(self, 'min_elevation_duration', n.get_object_value(Timedelta)),
            "notification_to_user_on_elevation": lambda n : setattr(self, 'notification_to_user_on_elevation', n.get_bool_value()),
            "ticketing_info_on_elevation": lambda n : setattr(self, 'ticketing_info_on_elevation', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_mfa_on_elevation_configurable(self,) -> Optional[bool]:
        """
        Gets the isMfaOnElevationConfigurable property value. true if mfaOnElevation is configurable. false if mfaOnElevation is not configurable.
        Returns: Optional[bool]
        """
        return self._is_mfa_on_elevation_configurable
    
    @is_mfa_on_elevation_configurable.setter
    def is_mfa_on_elevation_configurable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMfaOnElevationConfigurable property value. true if mfaOnElevation is configurable. false if mfaOnElevation is not configurable.
        Args:
            value: Value to set for the isMfaOnElevationConfigurable property.
        """
        self._is_mfa_on_elevation_configurable = value
    
    @property
    def last_global_admin(self,) -> Optional[bool]:
        """
        Gets the lastGlobalAdmin property value. Internal used only.
        Returns: Optional[bool]
        """
        return self._last_global_admin
    
    @last_global_admin.setter
    def last_global_admin(self,value: Optional[bool] = None) -> None:
        """
        Sets the lastGlobalAdmin property value. Internal used only.
        Args:
            value: Value to set for the lastGlobalAdmin property.
        """
        self._last_global_admin = value
    
    @property
    def max_elavation_duration(self,) -> Optional[Timedelta]:
        """
        Gets the maxElavationDuration property value. Maximal duration for the activated role.
        Returns: Optional[Timedelta]
        """
        return self._max_elavation_duration
    
    @max_elavation_duration.setter
    def max_elavation_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maxElavationDuration property value. Maximal duration for the activated role.
        Args:
            value: Value to set for the maxElavationDuration property.
        """
        self._max_elavation_duration = value
    
    @property
    def mfa_on_elevation(self,) -> Optional[bool]:
        """
        Gets the mfaOnElevation property value. true if MFA is required to activate the role. false if MFA is not required to activate the role.
        Returns: Optional[bool]
        """
        return self._mfa_on_elevation
    
    @mfa_on_elevation.setter
    def mfa_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the mfaOnElevation property value. true if MFA is required to activate the role. false if MFA is not required to activate the role.
        Args:
            value: Value to set for the mfaOnElevation property.
        """
        self._mfa_on_elevation = value
    
    @property
    def min_elevation_duration(self,) -> Optional[Timedelta]:
        """
        Gets the minElevationDuration property value. Minimal duration for the activated role.
        Returns: Optional[Timedelta]
        """
        return self._min_elevation_duration
    
    @min_elevation_duration.setter
    def min_elevation_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the minElevationDuration property value. Minimal duration for the activated role.
        Args:
            value: Value to set for the minElevationDuration property.
        """
        self._min_elevation_duration = value
    
    @property
    def notification_to_user_on_elevation(self,) -> Optional[bool]:
        """
        Gets the notificationToUserOnElevation property value. true if send notification to the end user when the role is activated. false if do not send notification when the role is activated.
        Returns: Optional[bool]
        """
        return self._notification_to_user_on_elevation
    
    @notification_to_user_on_elevation.setter
    def notification_to_user_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the notificationToUserOnElevation property value. true if send notification to the end user when the role is activated. false if do not send notification when the role is activated.
        Args:
            value: Value to set for the notificationToUserOnElevation property.
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
        writer.write_object_value("elevationDuration", self.elevation_duration)
        writer.write_bool_value("isMfaOnElevationConfigurable", self.is_mfa_on_elevation_configurable)
        writer.write_bool_value("lastGlobalAdmin", self.last_global_admin)
        writer.write_object_value("maxElavationDuration", self.max_elavation_duration)
        writer.write_bool_value("mfaOnElevation", self.mfa_on_elevation)
        writer.write_object_value("minElevationDuration", self.min_elevation_duration)
        writer.write_bool_value("notificationToUserOnElevation", self.notification_to_user_on_elevation)
        writer.write_bool_value("ticketingInfoOnElevation", self.ticketing_info_on_elevation)
    
    @property
    def ticketing_info_on_elevation(self,) -> Optional[bool]:
        """
        Gets the ticketingInfoOnElevation property value. true if the ticketing information is required when activate the role. false if the ticketing information is not required when activate the role.
        Returns: Optional[bool]
        """
        return self._ticketing_info_on_elevation
    
    @ticketing_info_on_elevation.setter
    def ticketing_info_on_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the ticketingInfoOnElevation property value. true if the ticketing information is required when activate the role. false if the ticketing information is not required when activate the role.
        Args:
            value: Value to set for the ticketingInfoOnElevation property.
        """
        self._ticketing_info_on_elevation = value
    

