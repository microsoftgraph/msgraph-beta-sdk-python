from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_flow import AuthenticationFlow
    from .conditional_access_client_app import ConditionalAccessClientApp
    from .conditional_access_device_platform import ConditionalAccessDevicePlatform
    from .device_info import DeviceInfo
    from .insider_risk_level import InsiderRiskLevel
    from .risk_level import RiskLevel

@dataclass
class ConditionalAccessWhatIfConditions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The authenticationFlow property
    authentication_flow: Optional[AuthenticationFlow] = None
    # The clientAppType property
    client_app_type: Optional[ConditionalAccessClientApp] = None
    # The country property
    country: Optional[str] = None
    # The deviceInfo property
    device_info: Optional[DeviceInfo] = None
    # The devicePlatform property
    device_platform: Optional[ConditionalAccessDevicePlatform] = None
    # The insiderRiskLevel property
    insider_risk_level: Optional[InsiderRiskLevel] = None
    # The ipAddress property
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The servicePrincipalRiskLevel property
    service_principal_risk_level: Optional[RiskLevel] = None
    # The signInRiskLevel property
    sign_in_risk_level: Optional[RiskLevel] = None
    # The userRiskLevel property
    user_risk_level: Optional[RiskLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessWhatIfConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessWhatIfConditions
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessWhatIfConditions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_flow import AuthenticationFlow
        from .conditional_access_client_app import ConditionalAccessClientApp
        from .conditional_access_device_platform import ConditionalAccessDevicePlatform
        from .device_info import DeviceInfo
        from .insider_risk_level import InsiderRiskLevel
        from .risk_level import RiskLevel

        from .authentication_flow import AuthenticationFlow
        from .conditional_access_client_app import ConditionalAccessClientApp
        from .conditional_access_device_platform import ConditionalAccessDevicePlatform
        from .device_info import DeviceInfo
        from .insider_risk_level import InsiderRiskLevel
        from .risk_level import RiskLevel

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationFlow": lambda n : setattr(self, 'authentication_flow', n.get_object_value(AuthenticationFlow)),
            "clientAppType": lambda n : setattr(self, 'client_app_type', n.get_enum_value(ConditionalAccessClientApp)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "deviceInfo": lambda n : setattr(self, 'device_info', n.get_object_value(DeviceInfo)),
            "devicePlatform": lambda n : setattr(self, 'device_platform', n.get_enum_value(ConditionalAccessDevicePlatform)),
            "insiderRiskLevel": lambda n : setattr(self, 'insider_risk_level', n.get_enum_value(InsiderRiskLevel)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipalRiskLevel": lambda n : setattr(self, 'service_principal_risk_level', n.get_enum_value(RiskLevel)),
            "signInRiskLevel": lambda n : setattr(self, 'sign_in_risk_level', n.get_enum_value(RiskLevel)),
            "userRiskLevel": lambda n : setattr(self, 'user_risk_level', n.get_enum_value(RiskLevel)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("authenticationFlow", self.authentication_flow)
        writer.write_enum_value("clientAppType", self.client_app_type)
        writer.write_str_value("country", self.country)
        writer.write_object_value("deviceInfo", self.device_info)
        writer.write_enum_value("devicePlatform", self.device_platform)
        writer.write_enum_value("insiderRiskLevel", self.insider_risk_level)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("servicePrincipalRiskLevel", self.service_principal_risk_level)
        writer.write_enum_value("signInRiskLevel", self.sign_in_risk_level)
        writer.write_enum_value("userRiskLevel", self.user_risk_level)
        writer.write_additional_data_value(self.additional_data)
    

