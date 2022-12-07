from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

microsoft_managed_desktop_type = lazy_import('msgraph.generated.models.microsoft_managed_desktop_type')

class MicrosoftManagedDesktop(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftManagedDesktop and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The name of the Microsoft Managed Desktop profile that the Windows 365 Cloud PC is associated with.
        self._profile: Optional[str] = None
        # Indicates whether the provisioning policy enables Microsoft Managed Desktop. It indicates the type of plan under which the device is managed if the provisioning policy is enabled. Possible values are: notManaged, premiumManaged, standardManaged, starterManaged, unknownFutureValue.
        self._type: Optional[microsoft_managed_desktop_type.MicrosoftManagedDesktopType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftManagedDesktop:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftManagedDesktop
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftManagedDesktop()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(microsoft_managed_desktop_type.MicrosoftManagedDesktopType)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def profile(self,) -> Optional[str]:
        """
        Gets the profile property value. The name of the Microsoft Managed Desktop profile that the Windows 365 Cloud PC is associated with.
        Returns: Optional[str]
        """
        return self._profile
    
    @profile.setter
    def profile(self,value: Optional[str] = None) -> None:
        """
        Sets the profile property value. The name of the Microsoft Managed Desktop profile that the Windows 365 Cloud PC is associated with.
        Args:
            value: Value to set for the profile property.
        """
        self._profile = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("profile", self.profile)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[microsoft_managed_desktop_type.MicrosoftManagedDesktopType]:
        """
        Gets the type property value. Indicates whether the provisioning policy enables Microsoft Managed Desktop. It indicates the type of plan under which the device is managed if the provisioning policy is enabled. Possible values are: notManaged, premiumManaged, standardManaged, starterManaged, unknownFutureValue.
        Returns: Optional[microsoft_managed_desktop_type.MicrosoftManagedDesktopType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[microsoft_managed_desktop_type.MicrosoftManagedDesktopType] = None) -> None:
        """
        Sets the type property value. Indicates whether the provisioning policy enables Microsoft Managed Desktop. It indicates the type of plan under which the device is managed if the provisioning policy is enabled. Possible values are: notManaged, premiumManaged, standardManaged, starterManaged, unknownFutureValue.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

