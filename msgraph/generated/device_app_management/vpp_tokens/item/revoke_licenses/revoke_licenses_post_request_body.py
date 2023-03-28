from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class RevokeLicensesPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new revokeLicensesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The notifyManagedDevices property
        self._notify_managed_devices: Optional[bool] = None
        # The revokeUntrackedLicenses property
        self._revoke_untracked_licenses: Optional[bool] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RevokeLicensesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RevokeLicensesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RevokeLicensesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "notifyManagedDevices": lambda n : setattr(self, 'notify_managed_devices', n.get_bool_value()),
            "revokeUntrackedLicenses": lambda n : setattr(self, 'revoke_untracked_licenses', n.get_bool_value()),
        }
        return fields
    
    @property
    def notify_managed_devices(self,) -> Optional[bool]:
        """
        Gets the notifyManagedDevices property value. The notifyManagedDevices property
        Returns: Optional[bool]
        """
        return self._notify_managed_devices
    
    @notify_managed_devices.setter
    def notify_managed_devices(self,value: Optional[bool] = None) -> None:
        """
        Sets the notifyManagedDevices property value. The notifyManagedDevices property
        Args:
            value: Value to set for the notify_managed_devices property.
        """
        self._notify_managed_devices = value
    
    @property
    def revoke_untracked_licenses(self,) -> Optional[bool]:
        """
        Gets the revokeUntrackedLicenses property value. The revokeUntrackedLicenses property
        Returns: Optional[bool]
        """
        return self._revoke_untracked_licenses
    
    @revoke_untracked_licenses.setter
    def revoke_untracked_licenses(self,value: Optional[bool] = None) -> None:
        """
        Sets the revokeUntrackedLicenses property value. The revokeUntrackedLicenses property
        Args:
            value: Value to set for the revoke_untracked_licenses property.
        """
        self._revoke_untracked_licenses = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("notifyManagedDevices", self.notify_managed_devices)
        writer.write_bool_value("revokeUntrackedLicenses", self.revoke_untracked_licenses)
        writer.write_additional_data_value(self.additional_data)
    

